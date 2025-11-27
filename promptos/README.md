# PromptOS 🧠

> A simple, file-based persona management system for Large Language Models

## The Philosophy

PromptOS is a lightweight, human-readable system for managing and switching between different "personas" or expert contexts when interacting with Large Language Models (LLMs). Think of it as an operating system for your AI interactions—where each persona is a specialized program designed to excel at specific tasks.

Instead of wrestling with complex prompt engineering or losing track of what works, PromptOS provides a structured, version-controllable approach to persona management. Each persona is a carefully crafted system prompt that transforms your LLM into a domain expert with specific values, communication styles, and output preferences.

## How It Works

PromptOS follows a simple directory structure:

```
promptos/
├── README.md                 # You are here
├── system_prompts/          # Core persona definitions
│   ├── 01_pragmatic_engineer.md
│   ├── 02_scribe.md
│   └── template_persona.md
├── code_snippets/           # (Optional) Reusable code patterns
└── workflows/               # (Optional) Multi-step processes
```

Each persona file is a markdown document containing:
- **Role Definition**: What expert role the LLM should embody
- **Core Values**: The principles that guide responses
- **Output Preferences**: How information should be structured
- **Constraints**: Boundaries and limitations to maintain focus

## How to Use It

### Quick Start

1. **Browse Available Personas**: Navigate to the `system_prompts/` directory
2. **Select Your Expert**: Choose a persona that matches your task (e.g., `01_pragmatic_engineer.md` for coding)
3. **Copy the Content**: Select all text from your chosen persona file
4. **Activate the Persona**: 
   - **In Cursor**: Paste into the system prompt field (⌘+, → Features → System Prompt)
   - **In ChatGPT**: Start a new conversation with the persona text
   - **In Claude**: Paste as the first message in your conversation
   - **In Other LLMs**: Use as the initial context or system message

### Example Workflow

```bash
# Working on a complex architecture problem?
→ Use 01_pragmatic_engineer.md

# Writing documentation or a blog post?
→ Use 02_scribe.md

# Need something specific?
→ Copy template_persona.md and create your own!
```

## Customization

### Creating Your Own Personas

1. **Start with the Template**: Copy `template_persona.md`
2. **Define the Role**: Be specific about expertise and perspective
3. **Set Clear Values**: What principles should guide the responses?
4. **Specify Output Format**: Tables? Code? Narrative? Be explicit
5. **Add Constraints**: What should the persona avoid or always include?

### Best Practices

- **Be Specific**: "Senior DevOps Engineer specializing in Kubernetes" > "Technical person"
- **Include Examples**: Show the persona what good output looks like
- **Version Control**: Track changes to your personas in git
- **Test and Iterate**: Refine based on actual usage
- **Share and Collaborate**: Great personas are worth sharing with your team

### Advanced Usage

**Persona Chaining**: Use different personas for different phases of a project:
1. Start with `pragmatic_engineer` for system design
2. Switch to `scribe` for documentation
3. Use a custom `code_reviewer` persona for final review

**Persona Mixing**: Combine elements from multiple personas for hybrid expertise

**Context Preservation**: When switching personas mid-conversation, include a brief handoff note to maintain context

## Why PromptOS?

- **🎯 Consistency**: Get reliable, predictable outputs every time
- **📁 Organized**: No more lost prompts in chat history
- **🔄 Reusable**: Build a library of expert personas
- **👥 Shareable**: Collaborate with team members using the same personas
- **📝 Version Controlled**: Track improvements and changes over time
- **🚀 Immediate**: Zero setup, just copy and paste

## Contributing

Found a great persona that others might benefit from? We welcome contributions! 

1. Create your persona using the template
2. Test it thoroughly in real scenarios
3. Submit a pull request with examples of its effectiveness

## License

PromptOS is part of the neuro-spicy-devkit and is available under the same open-source license. Use it, modify it, share it—make it yours.

---

*Remember: The best prompt is the one that works for you. Start simple, iterate often, and build your personal board of advisors.*