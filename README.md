# group_registration_server: Tasks List

- [ ] Google-based APIs
  - [ ] Google Groups
    - [ ] **GILAD** is_yacv_member(email)
    - [ ] **GILAD** add_member_to_group(email)
  - [ ] DB Tasks
    - [ ] **GILAD** CRUD on a challenged table (cols: email, referee, createdAt, approved [yes/no], approvedAt)
    - [ ] **question** should we insert to db if user is not approved?
- [ ] Flows
    - [ ] Traditional - **LEIGH** Referring an existing member
    - [ ] Extra check - Not referring an existing member (needing manual revewing)
- [ ] Notifications
    - **LEIGH** - Email Sending Service (inhouse)
    - Email templates
- [ ] Devops & Monitoring
    - [ ] DDOS Protection 
    - [ ] Sending exceptions to the email for maintainers of the project (via very same service? might defeat the purpose if the issue is with mail sending)
    - [ ] Exceptions handeling and approval
- [ ] UI - **GILAD**
