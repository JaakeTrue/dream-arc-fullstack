import React from 'react';

interface Note {
  id: string;
  content: string;
}

export default function NotesSection({ notes }: { notes: Note[] }) {
  return (
    <div className="notes-section">
      {notes.map(note => (
        <div key={note.id} className="note-card">
          {note.content}
        </div>
      ))}
    </div>
  )
}
