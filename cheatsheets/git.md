# Git
## Websites
* <https://git-scm.com/doc>
* <https://lab.github.com/>
* <https://github.com/dictcp/awesome-git>
* <https://github.com/sdras/awesome-actions>

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


# Best Practices

* Commit early, commit often.
* Atomic commits. (same fix/feature, same file.)
* Complete and tested commits.
* Meaningful commit messages.
	* max 50 characters.
	* imperative present tense.
* Never rebase.
* Release tags should be immutable and distinct from the marketing release.
	* Release tag: "2.0.0" and Marketing tag "Fizz Buzz".
	* It allows to have immutable tags and avoids take-backs.

