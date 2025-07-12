import React from 'react';
import './NotesSection.css';

interface Note {
  id: string;
  content: string;
  created_at: string;
}

export default function NotesSection({ notes }: { notes: Note[] }) {
  return (
    <div className="notes-container">
      {notes.map(note => (
        <div key={note.id} className="note-card">
          <p>{note.content}</p>
          <small>{datetime.now().strftime('%Y-%m-%d')}</small>
        </div>
      ))}
    </div>
  )
}
