# Debugging Demonstration Guide (For Video Recording)

This guide outlines what to demonstrate in the 3-minute debugging video for the assignment.

## 🎥 Video Structure (3 minutes max)

### **Segment 1: Setup (30 seconds)**

1. Open VS Code with the project
2. Show the `.vscode/launch.json` file (debugging configurations)
3. Explain that you'll demonstrate debugging mastery

### **Segment 2: Setting Breakpoints (30 seconds)**

1. Open `src/task_manager.py`
2. Set a breakpoint in the `add_task()` method (line ~190)
3. Set a breakpoint in the `is_overdue()` method (line ~107)
4. Set a conditional breakpoint: right-click on a breakpoint, add condition `task_id == 1`
5. Show the breakpoints panel

### **Segment 3: Starting Debug Session (30 seconds)**

1. Select "Python: CLI - Add Task" from debug configurations
2. Press F5 or click the green play button
3. Show that the program stops at the first breakpoint
4. Explain the debug controls: Continue (F5), Step Over (F10), Step Into (F11), Step Out (Shift+F11)

### **Segment 4: Inspecting Variables (30 seconds)**

1. When stopped at breakpoint, hover over variables to see their values
2. Show the Variables panel on the left
3. Expand objects to see their properties
4. Show `self.tasks`, `self.next_id`, etc.

### **Segment 5: Watch Expressions (30 seconds)**

1. Add watch expressions:
   - `len(self.tasks)`
   - `task.title`
   - `task.priority`
2. Show how watch expressions update as you step through code
3. Demonstrate evaluating expressions in the Debug Console

### **Segment 6: Stepping Through Code (30 seconds)**

1. Step Over (F10) a few times to show line-by-line execution
2. Step Into (F11) a method call to see inside the function
3. Step Out (Shift+F11) to return to the caller
4. Show the Call Stack panel

### **Segment 7: Advanced Features (20 seconds)**

1. Show conditional breakpoints in action
2. Demonstrate inline values (values shown directly in code)
3. Show exception breakpoints (break when exceptions are raised)

### **Segment 8: Debugging Tests (10 seconds)**

1. Switch to "Python: Run Specific Test" configuration
2. Set breakpoint in a test
3. Show debugging unit tests

## 📋 Checklist of Features to Demonstrate

✅ **Breakpoints**

- [ ] Regular breakpoints
- [ ] Conditional breakpoints
- [ ] Logpoints (optional)

✅ **Stepping**

- [ ] Step Over (F10)
- [ ] Step Into (F11)
- [ ] Step Out (Shift+F11)
- [ ] Continue (F5)

✅ **Variable Inspection**

- [ ] Hovering over variables
- [ ] Variables panel
- [ ] Expanding object properties
- [ ] Modifying variable values (optional)

✅ **Watch Expressions**

- [ ] Adding watch expressions
- [ ] Evaluating complex expressions

✅ **Debug Console**

- [ ] Evaluating Python expressions
- [ ] Testing code snippets

✅ **Call Stack**

- [ ] Viewing call stack
- [ ] Navigating between stack frames

✅ **Debug Configurations**

- [ ] Multiple launch configurations
- [ ] Debugging CLI commands
- [ ] Debugging tests

## 🎬 Recommended Script

**[0:00-0:30] Introduction & Setup**

> "Hello, I'm demonstrating debugging in VS Code for the Task Manager CLI project.
> I've set up several debug configurations in launch.json for different scenarios.
> Let me show you how to debug this Python application."

**[0:30-1:00] Breakpoints**

> "First, I'll set breakpoints. Here in task_manager.py, I'm adding a breakpoint in add_task.
> I can also set conditional breakpoints - this one will only trigger when task_id equals 1.
> Now let's start debugging."

**[1:00-1:30] Stepping Through Code**

> "I've selected the 'CLI - Add Task' configuration and pressed F5.
> The debugger stops at my breakpoint. I can use F10 to step over,
> F11 to step into functions, and F5 to continue. Watch as I step through the code."

**[1:30-2:00] Variable Inspection**

> "I can inspect variables by hovering or using the Variables panel.
> See how self.tasks shows the current tasks, and I can expand objects to see all properties.
> The task object shows title, priority, and all attributes."

**[2:00-2:30] Watch Expressions & Debug Console**

> "I'll add watch expressions to monitor values. Here's len(self.tasks),
> and I can evaluate any Python expression in the Debug Console.
> Watch how the values update as I step through."

**[2:30-3:00] Call Stack & Wrap-up**

> "The Call Stack shows the execution path - we're in add_task, called from the CLI.
> I can click any frame to see that context. This demonstrates full debugging mastery:
> breakpoints, stepping, inspection, watches, and understanding program flow.
> These skills are essential for finding and fixing bugs efficiently."

## 🎯 Key Points to Emphasize

1. **Breakpoints are powerful** - Use them strategically, not randomly
2. **Stepping helps understand flow** - Step Over for overview, Step Into for details
3. **Variable inspection is crucial** - See actual values, not assumptions
4. **Watch expressions save time** - Monitor important values continuously
5. **Debug Console is interactive** - Test hypotheses in real-time
6. **Call Stack shows context** - Understand how you got to current position

## 🔧 Setup Before Recording

1. **Clean environment:**

   ```bash
   # Delete tasks.json and logs
   Remove-Item tasks.json -ErrorAction SilentlyContinue
   Remove-Item -Recurse logs -ErrorAction SilentlyContinue
   ```

2. **Close unnecessary panels** - Focus on code and debug panels

3. **Increase font size** - Make it readable in video

4. **Test debug configurations** - Ensure they all work

5. **Practice the flow** - Do a dry run before recording

## 📝 Tips for Great Video

- **Speak clearly** - Explain what you're doing
- **Go slowly** - Give viewers time to see what's happening
- **Point out important things** - Use cursor to highlight
- **Stay focused** - 3 minutes goes fast
- **Show mastery** - Demonstrate confidence with the tools

## 🎓 What the Professor is Looking For

- **Understanding of debugging concepts**
- **Proficiency with IDE debugging tools**
- **Ability to troubleshoot systematically**
- **Knowledge of when to use which debugging technique**
- **Practical application to real code**

Good luck with your video! 🚀
