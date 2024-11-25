# 🌟 Lucidia Open Prompter

A revolutionary AI-powered project orchestration system for Windsurf IDE, designed to enhance the development experience through intelligent prompting and context awareness.

## 🎯 Overview

Lucidia Open Prompter serves as an adaptive project orchestration AI that facilitates:
- Project setup and management
- Workflow optimization
- Debugging assistance
- Environment synchronization
- Context-aware code analysis

## 🚀 Features

### Core Capabilities
- 🎨 Intelligent UI Integration
  - Green text welcome messages for Windsurf
  - Red text for upcoming feature announcements
  - Cursor position awareness (coming soon)
  - Local vision integration (coming soon)

### Project Management
- 📁 Automatic Project Setup
  - Directory creation and organization
  - Context file generation
  - Documentation folder awareness

### MEGAPrompter System
Adjustable parameters through the MEGAPrompter message system:
- ⚡ `adjust_screenshot_time`
- 🔄 `adjust_context_gathering`
- 🎨 `adjust_AI_prompt_style`
- 📏 `adjust_prompting_length`
- 🔍 `adjust_prompt_depth`
- 📚 `enable custom user prompt indexing`

### Workflow Features
- 📸 Screenshot Analysis
- 🖱️ Cursor Tracking (Coming Soon)
- 👁️ Local Vision Integration (Coming Soon)
- 🤖 Multi-Agent Coder Version (Coming Soon)

## 🛠️ Installation

1. Clone the repository:
```bash
git clone https://github.com/ExpressionsBot/Lucidia-Open-Prompter.git
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

## 💻 Usage

1. Start Open Interpreter
2. Select "Lucidia Windsurf Open Mode" (Option 2)
3. Follow the interactive prompts:
   - Provide project details or create a new project
   - Configure MEGAPrompter settings
   - Begin your development workflow

## 🔧 Configuration

The system maintains a `context.json` file that stores:
- Project activity status
- Directory paths
- Custom settings
- User preferences

## 🤝 Contributing

We welcome contributions! Feel free to:
- Submit bug reports
- Propose new features
- Create pull requests
- Improve documentation

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🌈 Future Roadmap

- Cursor tracking implementation
- Enhanced local vision capabilities
- Multi-agent coding system
- Advanced UI element detection
- Expanded workflow automation

## 🙏 Acknowledgments

Special thanks to:
- The Open Interpreter community
- Windsurf IDE team
- All contributors and supporters

## 🔬 Development Notes

### Current Implementation Status

#### Core System
- ✅ Basic project structure
- ✅ Context management system
- ✅ Settings persistence
- ✅ Colored terminal interface
- ✅ Screenshot capture functionality
- ✅ Logging system
- ✅ Project directory management

#### MEGAPrompter System
- ✅ Command interface
- ✅ Settings adjustment
- ✅ Context file generation
- ✅ Project state tracking
- ⏳ Custom prompt indexing (In Progress)
- ⏳ Deep context gathering (In Progress)

#### UI Integration
- ✅ Welcome messages
- ✅ Color-coded interface
- ⏳ Cursor position tracking
- ❌ Local vision integration
- ❌ UI element detection

#### Windsurf Integration
- ✅ Mode selection in Open Interpreter
- ✅ Basic workspace awareness
- ❌ Cursor tracking
- ❌ Multi-agent system
- ❌ Auto-documentation

### Development Roadmap

#### Phase 1 (Current)
- [x] Basic framework implementation
- [x] Context management
- [x] Project setup automation
- [x] Settings system
- [ ] Documentation folder detection
- [ ] File tree awareness

#### Phase 2 (Next)
- [ ] Cursor position tracking
- [ ] Screenshot analysis improvements
- [ ] Workspace state management
- [ ] Enhanced error handling
- [ ] Test suite implementation

#### Phase 3 (Planned)
- [ ] Local vision integration
- [ ] Multi-agent system
- [ ] Advanced UI detection
- [ ] Auto-documentation generation
- [ ] Custom prompt templates

### Architecture Notes

#### Context Management
```json
{
    "active": boolean,
    "project_directory": string,
    "last_activity": timestamp,
    "settings": {
        "screenshot_time": float,
        "context_gathering": string,
        "prompt_style": string,
        "prompt_length": string,
        "prompt_depth": string,
        "custom_prompt_index": string
    },
    "workspace_state": {
        "open_files": array,
        "cursor_positions": object,
        "last_screenshot": string
    }
}
```

#### Key Components
1. **LucidiaOpenPrompter**
   - Main orchestration class
   - Handles initialization and context management
   - Manages settings and configurations

2. **Context System**
   - JSON-based state persistence
   - Automatic context file generation
   - Settings management

3. **Screen Capture**
   - Automated screenshot functionality
   - Timestamp-based naming
   - Error handling and logging

4. **Command Interface**
   - Interactive command system
   - Setting adjustments
   - Project management

### Known Issues
1. Terminal interface needs better error handling
2. Screenshot capture may fail in certain environments
3. Context gathering depth is limited
4. Custom prompt indexing needs optimization

### Future Optimizations
1. Implement async screenshot capture
2. Add batch processing for context gathering
3. Improve error recovery mechanisms
4. Enhance logging detail level
5. Add performance metrics tracking
