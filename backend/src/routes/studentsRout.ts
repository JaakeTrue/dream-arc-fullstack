# Ensure directory exists
New-Item -ItemType Directory -Path "frontend/src/components/students" -Force

# Create the file with content
@"
import React from 'react';

interface Note {
  id: string;
  content: string;
}

interface Props {
  notes: Note[];
}

export default function NotesSection({ notes }: Props) {
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
"@ | Out-File -FilePath "frontend/src/components/students/NotesSection.tsx" -Encoding utf8