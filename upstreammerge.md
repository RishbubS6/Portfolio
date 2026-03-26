---
permalink: /upstreammerge
layout: post
---
# Syncing Your Template Portfolio with OCS Portfolio (Upstream)

## Why Not Just Drag and Drop?

When there are updates to the OCS Portfolio, you need those changes in your own repo. The manual approach — downloading files, dragging them in, hoping you didn't miss anything — is slow, error-prone, and easy to get wrong. You might overwrite your own work, miss a file, or copy something into the wrong folder without realizing it.

Git gives you a better way. By linking your personal repository to the original OCS Portfolio as an **upstream remote**, Git handles the comparison for you. It knows exactly what changed, what's new, and what you've already got. Instead of you eyeballing two folders, Git does the diff automatically and only brings in what's actually different. If there's a conflict between your code and the incoming update, it flags it clearly so you can decide what to keep, so your work doesnt get overwritten.

---

## First-Time Setup

Open your **Template Portfolio** project in VSCode, then run the following in your terminal:
```bash
cat .git/config # confirm you're in the correct "template portfolio" repo
git remote add upstream https://github.com/Open-Coding-Society/portfolio.git
git remote  # should now show both: origin and upstream
git fetch upstream # fetches upstream changes without merging yet
git merge upstream/main --allow-unrelated-histories
```

**What's happening here:**
- `git remote add upstream` tells Git "there's another version of this project I want to track" — in this case, your teacher's repo
- `git fetch upstream` downloads the latest changes from that repo without touching your files yet
- `git merge upstream/main` is where the magic happens — Git weaves the new updates into your project, preserving your own changes wherever possible

You may see **merge conflicts** appear in VSCode's Version Control panel. This just means both you and the upstream made changes to the same file. It's not an error, it just means Git wants you to confirm which version should be on your repository

- Open the merge conflict editor and select **Accept Incoming** to take all new updates
- After resolving each conflict, click **+** next to each file to move it to **Staged Changes**

Then verify everything looks good:
```bash
git status   # confirm the merge completed cleanly
make refresh # preview the result and check for visible updates
```

- Test locally to confirm new code is present
- In the **VSCode Version Control** tab, write a commit message and click **Sync**

---

## Regular Sync (After First-Time Setup)

Once the upstream remote is set up, staying current takes just two commands:
```bash
git fetch upstream
git merge upstream/main
```

Thats all you have to do. From here the routine is the same:

- Resolve any merge conflicts in VSCode
- Test locally to make sure everything works
- Sync via VSCode Version Control to push your updated repo

