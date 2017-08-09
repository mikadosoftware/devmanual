No one's perfect with this stuff.
If you don't believe me, clone git itself ($ git clone https://github.com/git/git) and open up the repo in tig(1)
https://github.com/jonas/tig
To be honest, I only in the past 2 years even bothered to view ($ git log --graph). Regardless of --graph getting wide now and then, I always visualize my git history as a straight line.
Also, sometimes having a non-linear history is inevitable. Especially in large open source projects where you're pulling in patches to a branch, and patches on top of that. You're not always going to be merging a branch with a single author straight onto master.
Despite posts like this (http://www.bitsnbites.eu/a-tidy-linear-git-history/) encouraging good git hygiene, I've had multiple open source projects merge in code via GitHub and never had negative consequence for it :P
Maybe there are corner cases where git bisect wouldn't work? Though I never used git bisect even once. Most I do is scroll through tig and view diffs. Also used to play with a cool git plugin in vim (https://github.com/tpope/vim-fugitive).
Also, GitHub has (since that linear git history post) introduced Rebase + Merge https://github.com/blog/2243-rebase-and-merge-pull-requests. I think that'll get you what you want.
I do keep branches ("pull requests" if you're using GH lingo) up to date with ($ git pull --rebase). That does mean a force push ($ git push --force), but it's ok if it's your personal branch. I also use interactive mode ($ git rebase -i <sha>) to edit/blend multiple commits.
Also, when I do merge, if I go through CLI, I'll preserve the history of the branch by not doing fast forwards ($ git merge <branch> --no-ff).