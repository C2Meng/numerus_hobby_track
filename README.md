# numerus_hobby_track
Problem: Have many hobby, no time to do all, how?

Backend
    • Python
    • Django
    • Django ORM
    • SQLite (default Django DB)

Frontend
    • Django Templates
    • HTML
    • CSS
    • Vanilla JavaScript


Version Control
    Git
    GitHub

Core Features 
1️ Add Hobby
User can create hobby.
Example:
Gaming
Priority: 3
Time/week: 5 hours

2️ List Hobby by Priority
Sort hobbies by priority.
Example output:
1. Video Editing
2. Poster Design
3. Gaming
4. Drawing
5. Graphic Design


3️ Allocate Time to Hobby
User can set:
Total free time per week
Example:
Free time = 20 hours
System distributes time based on priority.
Example output:

Video Editing – 6h\
Poster Design – 5h\
Gaming – 4h\
Drawing – 3h\
Graphic Design – 2h

4️ Weekly Time Scheduler
Simple schedule generator
Example:

Monday
  Gaming - 1h

Tuesday
  Video Editing - 2h

Wednesday
  Poster Design - 2h
Simple algorithm:
    • Sort hobbies by priority
Fill available time slots
