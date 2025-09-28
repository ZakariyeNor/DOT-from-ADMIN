# SAMS — Secret Agent Management System

SAMS is a **full-stack Django application** designed to manage missions, agents, and reporting for a secure operations environment. It integrates **Django OAuth Toolkit (DOT)** for authentication and authorization, allowing client apps to access resources with proper scopes and tokens.

---

## Table of Contents

1. [Project Overview](#project-overview)  
2. [Features](#features)  
3. [Project Structure](#project-structure)  
4. [Models](#models)  
5. [Views & URLs](#views--urls)  
6. [Templates & Static Files](#templates--static-files)  
7. [Permissions & DOT Scopes](#permissions--dot-scopes)  
8. [Reporting Service](#reporting-service)  
9. [Admin & Role Management](#admin--role-management)  
10. [Deployment](#deployment)  
11. [Future Enhancements](#future-enhancements)

---

## Project Overview

SAMS is designed to track:

- **Agents** — Unique code, rank, status, assigned missions.  
- **Missions** — Type, status, start/end dates, assigned agents, progress tracking.  
- **Reports** — Mission reports submitted by agents with approval workflow.  

The system supports **role-based access** for Field Agents, Analysts, and Directors, with frontend and backend permission checks. Integration with **Django OAuth Toolkit** ensures secure API access for authorized client apps.

---

## Features

- CRUD operations for **Agents** and **Missions**  
- **Role-based access control** with custom permissions  
- **Mission logs** to track updates and progress  
- **Reporting Service** with submission, approval, and audit logging  
- DOT-protected API endpoints with **scopes**: `read_report`, `write_report`, `admin_report`  
- Notification system for agents (via Django messages or emails)  
- Reporting dashboard with **charts** and filters  
- Fully responsive templates with CSS styling  

---

## Project Structure

```bash
sams_project/
├─ agents/
│ ├─ migrations/
│ ├─ templates/agents/
│ │ ├─ agent_list.html
│ │ ├─ mission_detail.html
│ │ └─ ...
│ ├─ models.py
│ ├─ views.py
│ ├─ urls.py
│ ├─ admin.py
│ └─ forms.py
├─ reports/
│ ├─ templates/reports/
│ ├─ models.py
│ ├─ views.py
│ ├─ urls.py
│ └─ admin.py
├─ sams_project/
│ ├─ settings.py
│ ├─ urls.py
│ ├─ wsgi.py
│ └─ asgi.py
├─ templates/
│ ├─ base.html
│ └─ home.html
├─ static/
│ ├─ css/
│ ├─ js/
│ └─ images/
└─ manage.py
```

---

## Models

### Agent Model
- Links to `User` model (`OneToOneField`)
- Fields: `agent_code`, `rank`, `status`, `assigned_missions`
- Permissions: `can_assign_mission`, `can_change_status`

### Mission Model
- Fields: `name`, `description`, `mission_type`, `status`, `start_date`, `end_date`, `progress_percentage`, `agents`
- Related `MissionLog` for tracking updates

### Report Model
- Fields: `mission`, `author`, `content`, `submitted_at`, `status`
- Workflow: `draft`, `submitted`, `approved`, `rejected`
- DOT scopes for API access

---

## Views & URLs

### Agents
- List agents: `/agents/`  
- Change agent status: `/agents/<agent_id>/status/<new_status>/`

### Missions
- List missions: `/missions/`  
- Create mission: `/missions/create/`  
- Mission detail: `/missions/<pk>/`  
- Assign agent: `/missions/<mission_id>/assign/<agent_id>/`  
- Update mission status & add log: `/missions/<pk>/update_status/`

### Reports (DOT Protected)
- Submit report: `/reports/create/` (requires `write_report`)  
- List reports: `/reports/` (requires `read_report`)  
- Update report: `/reports/<pk>/edit/` (author or admin only)  
- Approve/reject report: `/reports/<pk>/approve/` or `/reports/<pk>/reject/` (admin only)

---

## Templates & Static Files

- `base.html` — main layout with header, footer, and blocks  
- `agent_list.html`, `mission_detail.html`, `report_form.html`, etc.  
- Static files: CSS, JS, images organized under `/static/`  
- Buttons and actions styled with `.btn`, `.btn-danger`, `.btn-success`, `.btn-warning`  

---

## Permissions & DOT Scopes

### Roles
- **Field Agent**: Basic access, cannot assign missions  
- **Analyst**: Can create missions  
- **Director**: Can assign missions, change status, approve reports

### DOT Scopes
- `read_report` — View reports  
- `write_report` — Create/edit own reports  
- `admin_report` — Full admin access  

---

## Reporting Service

- Tracks mission reports with status and author  
- Log report submissions, edits, approvals, and deletions  
- Provides dashboards with counts, recent submissions, and charts  
- Notifications for status changes to agents  

---

## Admin & Role Management

- Use Django admin to assign permissions and roles  
- Admin can filter missions, agents, and reports  
- Audit logging enabled via Django signals  

---

## Deployment

- Dockerized for easy deployment  
- Use HTTPS for all endpoints  
- DOT-protected API endpoints tested with tokens and scopes  
- Environment variables for secrets and credentials  

---

## Future Enhancements

- Mobile-friendly PWA support  
- More advanced reporting charts and filters  
- Email/SMS notifications for critical mission updates  
- Integration with external client apps via OAuth2  

---

## License

MIT License © 2025  

---

