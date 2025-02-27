## Créer une liste partagée entre plusieurs composants

### TaskList.js
```javascript
// TaskList.js
import React from 'react';

function TaskList({ tasks }) {
    return (
        <ul>
            {tasks.map((task, index) => (
                <li key={index}>{task}</li>
            ))}
        </ul>
    );
}

export default TaskList;
```

### TaskInput.js
```javascript
// TaskInput.js
import React, { useState } from 'react';

function TaskInput({ onAddTask }) {
    const [newTask, setNewTask] = useState('');

    const handleAdd = () => {
        if (newTask.trim()) {
            onAddTask(newTask);
            setNewTask('');
        }
    };

    return (
        <div>
            <input
                type="text"
                value={newTask}
                onChange={(e) => setNewTask(e.target.value)}
                placeholder="Nouvelle tâche"
            />
            <button onClick={handleAdd}>Ajouter une tâche</button>
        </div>
    );
}

export default TaskInput;
```

### TaskControls.js
```javascript
// TaskControls.js
import React from 'react';

function TaskControls({ onClearTasks }) {
    return <button onClick={onClearTasks}>Vider la liste</button>;
}

export default TaskControls;
```

### App.js
```javascript
// App.js
import React, { useState } from 'react';
import TaskList from './TaskList';
import TaskInput from './TaskInput';
import TaskControls from './TaskControls';

function App() {
    const [tasks, setTasks] = useState([]);

    const addTask = (task) => setTasks((prevTasks) => [...prevTasks, task]);
    const clearTasks = () => setTasks([]);

    return (
        <div>
            <TaskInput onAddTask={addTask} />
            <TaskList tasks={tasks} />
            <TaskControls onClearTasks={clearTasks} />
        </div>
    );
}

export default App;
```