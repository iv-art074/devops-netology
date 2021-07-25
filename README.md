iv_ar@Pappa MINGW64 ~/documents/github/devops-netology/branching (main)
$ git add merge.sh

iv_ar@Pappa MINGW64 ~/documents/github/devops-netology/branching (main)
$ git commit -m 'prepare for merge and rebase'
[main 2096032] prepare for merge and rebase
 1 file changed, 2 insertions(+), 2 deletions(-)

iv_ar@Pappa MINGW64 ~/documents/github/devops-netology/branching (main)
$ git push origin main
To https://github.com/iv-art074/devops-netology.git
 ! [rejected]        main -> main (non-fast-forward)
error: failed to push some refs to 'https://github.com/iv-art074/devops-netology.git'
hint: Updates were rejected because the tip of your current branch is behind
hint: its remote counterpart. Integrate the remote changes (e.g.
hint: 'git pull ...') before pushing again.
hint: See the 'Note about fast-forwards' in 'git push --help' for details.

iv_ar@Pappa MINGW64 ~/documents/github/devops-netology/branching (main)
$ git pull origin main
From https://github.com/iv-art074/devops-netology
 * branch            main       -> FETCH_HEAD
Merge made by the 'recursive' strategy.
 Terraform/readme.md | 4 ++--
 1 file changed, 2 insertions(+), 2 deletions(-)


iv_ar@Pappa MINGW64 ~/documents/github/devops-netology/branching (main)
$ vim merge.sh

iv_ar@Pappa MINGW64 ~/documents/github/devops-netology/branching (main)
$ git add merge.sh

iv_ar@Pappa MINGW64 ~/documents/github/devops-netology/branching (main)
$ ls -lh
total 2.0K
-rwxr-xr-x 1 iv_ar 197609 156 Jul 25 11:31 merge.sh*
-rwxr-xr-x 1 iv_ar 197609 155 Jul 25 11:09 rebase.sh*

iv_ar@Pappa MINGW64 ~/documents/github/devops-netology/branching (main)
$ git commit -m 'prepare for merge and rebase'
On branch main
Your branch is ahead of 'gitlab/main' by 4 commits.
  (use "git push" to publish your local commits)

nothing to commit, working tree clean

iv_ar@Pappa MINGW64 ~/documents/github/devops-netology/branching (main)
$ git push origin main
Enumerating objects: 14, done.
Counting objects: 100% (14/14), done.
Delta compression using up to 8 threads
Compressing objects: 100% (11/11), done.
Writing objects: 100% (12/12), 1.96 KiB | 1.96 MiB/s, done.
Total 12 (delta 3), reused 0 (delta 0), pack-reused 0
remote: Resolving deltas: 100% (3/3), done.
To https://github.com/iv-art074/devops-netology.git
   926266b..a90af13  main -> main

iv_ar@Pappa MINGW64 ~/documents/github/devops-netology/branching (main)
$ git checkout git-merge
Switched to branch 'git-merge'

iv_ar@Pappa MINGW64 ~/documents/github/devops-netology/branching (git-merge)
$ vim merge.sh


iv_ar@Pappa MINGW64 ~/documents/github/devops-netology/branching (git-merge)
$ git add merge.sh

iv_ar@Pappa MINGW64 ~/documents/github/devops-netology/branching (git-merge)
$ git commit -m 'merge: @ instead *'
[git-merge 9caa907] merge: @ instead *
 1 file changed, 2 insertions(+), 2 deletions(-)

iv_ar@Pappa MINGW64 ~/documents/github/devops-netology/branching (git-merge)
$ git push origin git-merge
Enumerating objects: 15, done.
Counting objects: 100% (15/15), done.
Delta compression using up to 8 threads
Compressing objects: 100% (12/12), done.
Writing objects: 100% (12/12), 1019 bytes | 1019.00 KiB/s, done.
Total 12 (delta 6), reused 0 (delta 0), pack-reused 0
remote: Resolving deltas: 100% (6/6), completed with 2 local objects.
remote:
remote: Create a pull request for 'git-merge' on GitHub by visiting:
remote:      https://github.com/iv-art074/devops-netology/pull/new/git-merge
remote:
To https://github.com/iv-art074/devops-netology.git
 * [new branch]      git-merge -> git-merge

iv_ar@Pappa MINGW64 ~/documents/github/devops-netology/branching (git-merge)
$ vim merge.sh

iv_ar@Pappa MINGW64 ~/documents/github/devops-netology/branching (git-merge)
$ git add merge.sh

iv_ar@Pappa MINGW64 ~/documents/github/devops-netology/branching (git-merge)
$ git commit -m 'merge: use shift'
[git-merge 4d87a47] merge: use shift
 1 file changed, 3 insertions(+), 3 deletions(-)

iv_ar@Pappa MINGW64 ~/documents/github/devops-netology/branching (git-merge)
$ git push origin git-merge
Enumerating objects: 7, done.
Counting objects: 100% (7/7), done.
Delta compression using up to 8 threads
Compressing objects: 100% (4/4), done.
Writing objects: 100% (4/4), 451 bytes | 451.00 KiB/s, done.
Total 4 (delta 1), reused 0 (delta 0), pack-reused 0
remote: Resolving deltas: 100% (1/1), completed with 1 local object.
To https://github.com/iv-art074/devops-netology.git
   9caa907..4d87a47  git-merge -> git-merge

iv_ar@Pappa MINGW64 ~/documents/github/devops-netology/branching (main)
$ vim rebase.sh

iv_ar@Pappa MINGW64 ~/documents/github/devops-netology/branching (main)
$ git add rebase.sh

iv_ar@Pappa MINGW64 ~/documents/github/devops-netology/branching (main)
$ git commit -m 'rebase changed'
[main a6884d4] rebase changed
 1 file changed, 5 insertions(+), 3 deletions(-)

iv_ar@Pappa MINGW64 ~/documents/github/devops-netology/branching (main)
$ git push origin main
Enumerating objects: 7, done.
Counting objects: 100% (7/7), done.
Delta compression using up to 8 threads
Compressing objects: 100% (4/4), done.
Writing objects: 100% (4/4), 384 bytes | 384.00 KiB/s, done.
Total 4 (delta 2), reused 0 (delta 0), pack-reused 0
remote: Resolving deltas: 100% (2/2), completed with 2 local objects.
To https://github.com/iv-art074/devops-netology.git
   a90af13..a6884d4  main -> main

iv_ar@Pappa MINGW64 ~/documents/github/devops-netology/branching (main)
$ git log
commit a6884d4adf7f9500aefa33fa933b48dd8aa62015 (HEAD -> main, origin/main, origin/HEAD)
Author: iv-art074 <iv_art@mail.ru>
Date:   Sun Jul 25 11:50:54 2021 +1000

    rebase changed

commit a90af137ddd29ba547f1a0e0d26fc0492d300f6f
Merge: 2096032 926266b
Author: iv-art074 <iv_art@mail.ru>
Date:   Sun Jul 25 11:28:53 2021 +1000

    Merge branch 'main' of https://github.com/iv-art074/devops-netology

commit 209603239fb0578290602beb6488fd65b3b715f3
Author: iv-art074 <iv_art@mail.ru>
Date:   Sun Jul 25 11:27:39 2021 +1000

    prepare for merge and rebase

commit 7cffdf12b299d2f233a78f33c1e7bfec58f81d5f
Author: iv-art074 <iv_art@mail.ru>
Date:   Sun Jul 25 11:11:32 2021 +1000
:...skipping...
commit a6884d4adf7f9500aefa33fa933b48dd8aa62015 (HEAD -> main, origin/main, orig
Author: iv-art074 <iv_art@mail.ru>
Date:   Sun Jul 25 11:50:54 2021 +1000

    rebase changed

commit a90af137ddd29ba547f1a0e0d26fc0492d300f6f
Merge: 2096032 926266b
Author: iv-art074 <iv_art@mail.ru>
Date:   Sun Jul 25 11:28:53 2021 +1000

    Merge branch 'main' of https://github.com/iv-art074/devops-netology

commit 209603239fb0578290602beb6488fd65b3b715f3
Author: iv-art074 <iv_art@mail.ru>
Date:   Sun Jul 25 11:27:39 2021 +1000

    prepare for merge and rebase

commit 7cffdf12b299d2f233a78f33c1e7bfec58f81d5f
Author: iv-art074 <iv_art@mail.ru>
Date:   Sun Jul 25 11:11:32 2021 +1000

    prepare for merge and rebase

commit 33affb1152112ddc1d8687a0d84ff5b5a207f926 (tag: v0.1, tag: v0.0, gitlab/ma
Author: iv-art074 <iv_art@mail.ru>
Date:   Fri Jul 16 20:44:23 2021 +1000

    add readme

commit 926266b36dd183898078cac47762013428fce5af
Author: iv-art074 <87374285+iv-art074@users.noreply.github.com>
Date:   Wed Jul 14 00:21:10 2021 +1000

    Update readme.md

commit 8a6a09decd94607254419f9889eb410d69912a3b
Author: iv-art074 <iv_art@mail.ru>
Date:   Wed Jul 14 00:14:13 2021 +1000

    Moved and deleted

commit ec8f3d3937cb98927b1615c36c31abc779b19570
Author: iv-art074 <iv_art@mail.ru>
Date:   Wed Jul 14 00:12:38 2021 +1000

    Prepare to delete and move

commit f8f01a13caaa39fe9c9b84f2fdc971b2bc58ba49
Author: iv-art074 <iv_art@mail.ru>
Date:   Wed Jul 14 00:10:16 2021 +1000

    Added gitignore

commit d20e8660a73311f3f08051e153a9e15431482380
Author: Igor Art <iv_art@mail.ru>
Date:   Tue Jul 13 23:57:51 2021 +1000

    First commit

commit 11c2927caa6a981e355eb106848678a6e64c0e52
Author: Igor Art <iv_art@mail.ru>
Date:   Tue Jul 13 23:52:31 2021 +1000

    Create .gitconfig

commit 23a4d037bf2d6d3011efdfdeb0989380181f3860
Author: iv-art074 <87374285+iv-art074@users.noreply.github.com>
Date:   Tue Jul 13 23:00:20 2021 +1000

    Initial commit
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~

iv_ar@Pappa MINGW64 ~/documents/github/devops-netology/branching (main)
$ git checkout 209603239fb0578290602beb6488fd65b3b715f3
Note: switching to '209603239fb0578290602beb6488fd65b3b715f3'.

You are in 'detached HEAD' state. You can look around, make experimental
changes and commit them, and you can discard any commits you make in this
state without impacting any branches by switching back to a branch.

If you want to create a new branch to retain commits you create, you may
do so (now or later) by using -c with the switch command. Example:

  git switch -c <new-branch-name>

Or undo this operation with:

  git switch -

Turn off this advice by setting config variable advice.detachedHead to false

HEAD is now at 2096032 prepare for merge and rebase

iv_ar@Pappa MINGW64 ~/documents/github/devops-netology/branching ((2096032...))
$ git switch -c git-rebase
Switched to a new branch 'git-rebase'

iv_ar@Pappa MINGW64 ~/documents/github/devops-netology/branching (git-rebase)
$ vim rebase.sh

iv_ar@Pappa MINGW64 ~/documents/github/devops-netology/branching (git-rebase)
$ git add rebase.sh

iv_ar@Pappa MINGW64 ~/documents/github/devops-netology/branching (git-rebase)
$ git commit -m 'git-rebase 1'
[git-rebase 873f9f0] git-rebase 1
 1 file changed, 6 insertions(+), 3 deletions(-)

iv_ar@Pappa MINGW64 ~/documents/github/devops-netology/branching (git-rebase)
$ git push origin git-rebase
Enumerating objects: 7, done.
Counting objects: 100% (7/7), done.
Delta compression using up to 8 threads
Compressing objects: 100% (4/4), done.
Writing objects: 100% (4/4), 394 bytes | 394.00 KiB/s, done.
Total 4 (delta 2), reused 0 (delta 0), pack-reused 0
remote: Resolving deltas: 100% (2/2), completed with 2 local objects.
remote:
remote: Create a pull request for 'git-rebase' on GitHub by visiting:
remote:      https://github.com/iv-art074/devops-netology/pull/new/git-rebase
remote:
To https://github.com/iv-art074/devops-netology.git
 * [new branch]      git-rebase -> git-rebase

iv_ar@Pappa MINGW64 ~/documents/github/devops-netology/branching (git-rebase)
$ vim rebase.sh

iv_ar@Pappa MINGW64 ~/documents/github/devops-netology/branching (git-rebase)
$ git add rebase.sh

iv_ar@Pappa MINGW64 ~/documents/github/devops-netology/branching (git-rebase)
$ git commit -m 'git-rebase 2'
[git-rebase 739de53] git-rebase 2
 1 file changed, 2 insertions(+), 1 deletion(-)

iv_ar@Pappa MINGW64 ~/documents/github/devops-netology/branching (git-rebase)
$ git push origin git-rebase
Enumerating objects: 7, done.
Counting objects: 100% (7/7), done.
Delta compression using up to 8 threads
Compressing objects: 100% (4/4), done.
Writing objects: 100% (4/4), 365 bytes | 365.00 KiB/s, done.
Total 4 (delta 2), reused 0 (delta 0), pack-reused 0
remote: Resolving deltas: 100% (2/2), completed with 2 local objects.
To https://github.com/iv-art074/devops-netology.git
   873f9f0..739de53  git-rebase -> git-rebase

iv_ar@Pappa MINGW64 ~/documents/github/devops-netology/branching (main)
$ git checkout git-merge
Switched to branch 'git-merge'

iv_ar@Pappa MINGW64 ~/documents/github/devops-netology/branching (git-merge)
$ git merge main
Updating 4d87a47..b33bad7
Fast-forward
 Terraform/readme.md | 4 ++--
 branching/merge.sh  | 8 ++++++--
 branching/rebase.sh | 8 +++++---
 3 files changed, 13 insertions(+), 7 deletions(-)

iv_ar@Pappa MINGW64 ~/documents/github/devops-netology/branching (git-merge)
$ git push
fatal: The current branch git-merge has no upstream branch.
To push the current branch and set the remote as upstream, use

    git push --set-upstream origin git-merge


iv_ar@Pappa MINGW64 ~/documents/github/devops-netology/branching (main)
$ git checkout git-merge
Switched to branch 'git-merge'


iv_ar@Pappa MINGW64 ~/documents/github/devops-netology/branching (git-merge)
$  git push --set-upstream origin git-merge
Enumerating objects: 10, done.
Counting objects: 100% (10/10), done.
Delta compression using up to 8 threads
Compressing objects: 100% (4/4), done.
Writing objects: 100% (4/4), 403 bytes | 403.00 KiB/s, done.
Total 4 (delta 2), reused 0 (delta 0), pack-reused 0
remote: Resolving deltas: 100% (2/2), completed with 2 local objects.
To https://github.com/iv-art074/devops-netology.git
   4d87a47..b33bad7  git-merge -> git-merge
Branch 'git-merge' set up to track remote branch 'git-merge' from 'origin'.

iv_ar@Pappa MINGW64 ~/documents/github/devops-netology/branching (git-merge)
$ git checkout git-rebase
Switched to branch 'git-rebase'

iv_ar@Pappa MINGW64 ~/documents/github/devops-netology/branching (git-rebase)
$ git rebase -i main
error: could not apply 873f9f0... git-rebase 1
Resolve all conflicts manually, mark them as resolved with
"git add/rm <conflicted_files>", then run "git rebase --continue".
You can instead skip this commit: run "git rebase --skip".
To abort and get back to the state before "git rebase", run "git rebase --abort".
Could not apply 873f9f0... git-rebase 1
Auto-merging branching/rebase.sh
CONFLICT (content): Merge conflict in branching/rebase.sh

iv_ar@Pappa MINGW64 ~/documents/github/devops-netology/branching (git-rebase|REBASE 1/2)
$ vim rebase.sh

iv_ar@Pappa MINGW64 ~/documents/github/devops-netology/branching (git-rebase|REBASE 1/2)
$ git add rebase.sh

iv_ar@Pappa MINGW64 ~/documents/github/devops-netology/branching (git-rebase|REBASE 1/2)
$ git rebase --continue
[detached HEAD 868881b] continued
 1 file changed, 9 insertions(+), 1 deletion(-)
error: could not apply 739de53... git-rebase 2
Resolve all conflicts manually, mark them as resolved with
"git add/rm <conflicted_files>", then run "git rebase --continue".
You can instead skip this commit: run "git rebase --skip".
To abort and get back to the state before "git rebase", run "git rebase --abort".
Could not apply 739de53... git-rebase 2
Auto-merging branching/rebase.sh
CONFLICT (content): Merge conflict in branching/rebase.sh

iv_ar@Pappa MINGW64 ~/documents/github/devops-netology/branching (git-rebase|REBASE 2/2)
$ vim rebase.sh

iv_ar@Pappa MINGW64 ~/documents/github/devops-netology/branching (git-rebase|REBASE 2/2)
$ git add rebase.sh

iv_ar@Pappa MINGW64 ~/documents/github/devops-netology/branching (git-rebase|REBASE 2/2)
$ git rebase --continue
[detached HEAD fff2c41] git-rebase 2
 1 file changed, 6 insertions(+), 1 deletion(-)
Successfully rebased and updated refs/heads/git-rebase.

iv_ar@Pappa MINGW64 ~/documents/github/devops-netology/branching (git-rebase)
$ git push -u origin git-rebase
To https://github.com/iv-art074/devops-netology.git
 ! [rejected]        git-rebase -> git-rebase (non-fast-forward)
error: failed to push some refs to 'https://github.com/iv-art074/devops-netology.git'
hint: Updates were rejected because the tip of your current branch is behind
hint: its remote counterpart. Integrate the remote changes (e.g.
hint: 'git pull ...') before pushing again.
hint: See the 'Note about fast-forwards' in 'git push --help' for details.

iv_ar@Pappa MINGW64 ~/documents/github/devops-netology/branching (git-rebase)
$ git push -u origin git-rebase -f
Enumerating objects: 11, done.
Counting objects: 100% (11/11), done.
Delta compression using up to 8 threads
Compressing objects: 100% (8/8), done.
Writing objects: 100% (8/8), 785 bytes | 785.00 KiB/s, done.
Total 8 (delta 3), reused 0 (delta 0), pack-reused 0
remote: Resolving deltas: 100% (3/3), completed with 2 local objects.
To https://github.com/iv-art074/devops-netology.git
 + 739de53...fff2c41 git-rebase -> git-rebase (forced update)
Branch 'git-rebase' set up to track remote branch 'git-rebase' from 'origin'.

iv_ar@Pappa MINGW64 ~/documents/github/devops-netology/branching (git-rebase)
$ git chekout main
git: 'chekout' is not a git command. See 'git --help'.

The most similar command is
        checkout

iv_ar@Pappa MINGW64 ~/documents/github/devops-netology/branching (git-rebase)
$ git checkout main
Switched to branch 'main'
Your branch is up to date with 'origin/main'.

iv_ar@Pappa MINGW64 ~/documents/github/devops-netology/branching (main)
$ git merge git-rebase
Updating b33bad7..fff2c41
Fast-forward
 branching/rebase.sh | 17 +++++++++++++++--
 1 file changed, 15 insertions(+), 2 deletions(-)




