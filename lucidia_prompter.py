import os
import sys
import json
from PIL import ImageGrab
import logging
from datetime import datetime

class LucidiaOpenPrompter:
    """
    Lucidia Open Prompter: An intelligent project orchestration AI for Windsurf IDE.
    """
    
    def __init__(self, workspace_dir=None):
        self.workspace_dir = workspace_dir or os.getcwd()
        self.context_file = os.path.join(self.workspace_dir, "context.json")
        self.log_file = os.path.join(self.workspace_dir, "lucidia.log")
        self.setup_logging()
        self.initialize_context()

    def setup_logging(self):
        """Configure logging for the prompter."""
        logging.basicConfig(
            filename=self.log_file,
            level=logging.INFO,
            format='%(asctime)s - %(levelname)s - %(message)s'
        )
        self.logger = logging.getLogger('LucidiaPrompter')

    def initialize_context(self):
        """Initialize or load the context file."""
        if not os.path.exists(self.context_file):
            default_context = {
                "active": False,
                "project_directory": "",
                "last_activity": str(datetime.now()),
                "settings": {
                    "screenshot_time": 1.0,
                    "context_gathering": "standard",
                    "prompt_style": "default",
                    "prompt_length": "medium",
                    "prompt_depth": "standard",
                    "custom_prompt_index": ""
                },
                "workspace_state": {
                    "open_files": [],
                    "cursor_positions": {},
                    "last_screenshot": None
                }
            }
            with open(self.context_file, 'w') as f:
                json.dump(default_context, f, indent=4)
            self.context = default_context
        else:
            with open(self.context_file, 'r') as f:
                self.context = json.load(f)

    def capture_screen(self):
        """Capture the current screen state."""
        try:
            screenshot = ImageGrab.grab()
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            screenshot_dir = os.path.join(self.workspace_dir, "screenshots")
            os.makedirs(screenshot_dir, exist_ok=True)
            screenshot_path = os.path.join(screenshot_dir, f"screen_{timestamp}.png")
            screenshot.save(screenshot_path)
            self.context["workspace_state"]["last_screenshot"] = screenshot_path
            self.save_context()
            return screenshot_path
        except Exception as e:
            self.logger.error(f"Screen capture failed: {str(e)}")
            return None

    def display_welcome(self):
        """Display the welcome message with color coding."""
        print("\033[32m=== Welcome to Lucidia Open Prompter for Windsurf! ===\033[0m")
        print("\033[31m(Coming soon: cursor tracking, local vision, and multi-agent coder version)\033[0m")
        print("\nPlease provide project details or press Enter to start a new project:")

    def adjust_setting(self, setting_name, value):
        """Adjust a specific prompter setting."""
        if setting_name in self.context["settings"]:
            self.context["settings"][setting_name] = value
            self.save_context()
            self.logger.info(f"Setting '{setting_name}' updated to: {value}")
            return True
        return False

    def save_context(self):
        """Save the current context to file."""
        with open(self.context_file, 'w') as f:
            json.dump(self.context, f, indent=4)

    def start(self):
        """Start the Lucidia Open Prompter interface."""
        self.display_welcome()
        project_input = input().strip()
        
        if not project_input:
            print("Would you like to create a new project? (y/n)")
            if input().lower().startswith('y'):
                print("Enter project name:")
                project_name = input().strip()
                project_dir = os.path.join(self.workspace_dir, project_name)
                os.makedirs(project_dir, exist_ok=True)
                self.context["project_directory"] = project_dir
                self.context["active"] = True
                self.save_context()
                print(f"Created project directory: {project_dir}")
            else:
                print("Operation cancelled.")
                return

        print("\nMEGAPrompter Message:")
        print("Available commands:")
        print("- adjust_screenshot_time <seconds>")
        print("- adjust_context_gathering <standard|deep|shallow>")
        print("- adjust_AI_prompt_style <default|creative|technical>")
        print("- adjust_prompting_length <short|medium|long>")
        print("- adjust_prompt_depth <standard|detailed|minimal>")
        print("- enable_custom_prompt_indexing <path>")
        
        while True:
            command = input("\nEnter command (or 'exit' to quit): ").strip()
            if command.lower() == 'exit':
                break
            
            try:
                cmd_parts = command.split()
                if len(cmd_parts) >= 2:
                    setting = cmd_parts[0]
                    value = ' '.join(cmd_parts[1:])
                    if self.adjust_setting(setting, value):
                        print(f"Successfully updated {setting}")
                    else:
                        print(f"Unknown setting: {setting}")
                else:
                    print("Invalid command format. Use: setting_name value")
            except Exception as e:
                self.logger.error(f"Command execution failed: {str(e)}")
                print(f"Error executing command: {str(e)}")

if __name__ == "__main__":
    prompter = LucidiaOpenPrompter()
    prompter.start()
