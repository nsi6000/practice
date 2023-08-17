# Git
## Websites
* <https://git-scm.com/doc>
* <https://lab.github.com/>
* <https://github.com/dictcp/awesome-git>
* <https://github.com/sdras/awesome-actions>
* <https://semver.org/>
* <https://githooks.com/>
* <https://pre-commit.com/>
* <https://www.conventionalcommits.org/en/v1.0.0/>
* <https://github.com/tommarshall/git-good-commit>

## Commands
* git init
* git clone <repository_url>
* git config -e --global //edit the config gile for "global".
* git pull
* git add <file_name>|.|*.<file_extension>
* git commit -m "<commit_message>"
* git status
* git push
* git log (--graph) (--oneline) (--after="<date>") (--before="<date>") (--author="<user_name>") (--grep="<message>") (<source_branch>..<target_branch>)
* git commit --amend
* git reset (--soft) (--hard) <commit>
* git branch <branch-name>
* git checkout <commit_hash>|HEAD|<branch_name>
* git cherry-pick (-e) (-x)
* git diff HEAD
* git diff <commit> <commit> #git diff 0a52659 6aefce1 
* git diff origin/master -- vim.md #diff of local file vim.md with master.
* git log origin/master..master #list of all commits not yet pushed.

# Concepts

* commit
* branch
* pull and push
* rebase
* reset
* revert
* merge
* HEAD: last commit on the history.
* origin
* master: current official version of the code.
* remote
* pull request (PR): request to merge the commit into master branch.
* diff: set of changed lines within a single file.
* git merge methods:
	- Merge commit
	- Merge commit with semi-linear history (only fast-forward merge)
	- Fast-forward merge (no merge commit)

* conventional commits
* git hooks
* Git Flow
* pre-commit
* semver
* git good commit
* trunk-based development

# Best Practices

* Commit early, commit often.
* Atomic commits. (same fix/feature, same file.)
* Small diffs, small commits. (KISS)
* Protect main branch against direct commits. (cf pre-commit no-commit-to-branch)
* Don't push .git folder. (security risk. cf Github's WangYihang/GitHacker)
* Complete and tested commits.
* Meaningful commit messages.
	* max 50 characters.
	* imperative present tense.
* Never rebase.
* Never break the build.
* Short-lived branches.
* Release tags should be immutable and distinct from the marketing release.
	* Release tag: "2.0.0" and Marketing tag "Fizz Buzz".
	* It allows to have immutable tags and avoids take-backs.

# Git Flow
0. RTFM and ask questions.
0. git clone / git pull
1. git branch <branch_name>
2. git checkout <branch_name>
3. git branch
4. CODE (design_tests_alternatives - comments - red - green - refactor.)
5. LINT (checkpatch.pl - indent -kr|-linux <file>)
6. git status
7. git diff
8. BUILD/TEST (make M=<path>)
9. COMMIT (git commit -a)
10. short description - long description - signedoffby - ackedby - diff.
11. git log
12. git show --pretty=full
13. git format-patch master..<branch_name>
14. get_maintainer.pl <patch_name>.patch
15. git send-email --to <email> --cc <email> <patch>.patch
16. git blame <file>
17. Pull Request


