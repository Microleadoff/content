## Jouer avec les tableaux

### TaskManager.js
```javascript
import React, { useState } from 'react';

function TaskManager() {
    const [tasks, setTasks] = useState(['Tâche 1', 'Tâche 2']);
    const [newTask, setNewTask] = useState('');
    const [editIndex, setEditIndex] = useState(null);
    const [editValue, setEditValue] = useState('');

    const addTask = () => {
        if (newTask.trim()) {
            setTasks((prevTasks) => [...prevTasks, newTask]);
            setNewTask('');
        }
    };

    const deleteTask = (index) => {
        setTasks((prevTasks) => prevTasks.filter((_, i) => i !== index));
    };

    const editTask = (index) => {
        setEditIndex(index);
        setEditValue(tasks[index]);
    };

    const saveTask = () => {
        setTasks((prevTasks) =>
            prevTasks.map((task, i) => (i === editIndex ? editValue : task))
        );
        setEditIndex(null);
        setEditValue('');
    };

    return (
        <div>
            <h1>Gestionnaire de tâches</h1>
            <input
                type="text"
                value={newTask}
                onChange={(e) => setNewTask(e.target.value)}
                placeholder="Nouvelle tâche"
            />
            <button onClick={addTask}>Ajouter une tâche</button>
            <ul>
                {tasks.map((task, index) => (
                <li key={index}>
                    {editIndex === index ? (
                    <>
                        <input
                        type="text"
                        value={editValue}
                        onChange={(e) => setEditValue(e.target.value)}
                        />
                        <button onClick={saveTask}>Enregistrer</button>
                    </>
                    ) : (
                    <>
                        {task}
                        <button onClick={() => deleteTask(index)}>Supprimer</button>
                        <button onClick={() => editTask(index)}>Modifier</button>
                    </>
                    )}
                </li>
                ))}
            </ul>
        </div>
    );
}

export default TaskManager;
```

### App.js
```javascript
// App.js
import React from 'react';
import TaskManager from './TaskManager';

function App() {
    return (
        <div>
            <TaskManager />
        </div>
    );
}

export default App;
```