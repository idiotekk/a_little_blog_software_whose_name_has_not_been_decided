A high-level overview of the structure of the app.

The app consists of two parts:
1. Backend:
    Responsible for data storage, fetching and searching.
2. Frontend:
    In other words, the user interface (UI), which is repsonsible to interact with users.

# Backend 
3 components:
## database
Methods:
1. read raw files
2. save raw files

## post class
Has 3 attributes:
1. id, the unique identifier of each post.
2. meta, a dict that stores the meta data: title, labels, etc.
3. text, the body of the post in markdown language.

### how to implement a `template` class??
A template is a special post that has unfinished/skeleton, therefore can be a post with a `is_template` flag.

## github client
Able to:
1. connect to github
2. push to github
3. pull from github

# Frontend

## Main window
The "body" of the app that user spend most of the time interact with. 
Subordinate windows:
### Preview (optional)
A window to preview markdown text.
### msicelleneous windows
Varioius pop-up windows (progress bar, alerting, etc.) that react to user's actions.

## Initializing window
Popped up when user regitster the account, or change account.
