# Vim
## Websites
* <https://vimawesome.com/>
* <https://vim.fandom.com/>
* <https://github.com/mhinz/vim-galore>

vim file1 +line_number		open file at specified line number.
vim -o file1 file2		vertical window.
vim -O file1 file2		horizontal window.
CTRL+w hjkl			switch window.


## Commands
* :wq //write-quit
* :q! //discard-quit
* :w //write-save
* :sp //split
* :vs //vertical-split
* :set number //activate-line-numbering
* :reg //show-registers
* /foo //search-forward
* ?foo //search-backward
	* n //search-next
	* N //search-previous
* :%s/foo/bar/g //search-replace-global
* :%s/foo/bar/gn //count all abc.
* :!<command> //execute-shell-command
* :recover .orientdb.md.swp //recover a vim swap file.
* :r !ls *pdf		//read terminal command.
* :his			//history of commands.
* :h <string>		//show help of <string>.


* I //insert-BOL
* i //insert-mode
* a //append-cursor
* A //append-EOL
* o //newline-after
* O //newline-before

* 0 //move-BOL
* $ //move-EOL
* b //move-previous-word
* w //move-next-word
* gg //move-BOF
* GG //move-EOF
* 42gg //move-to-line-number

* v //visual-mode
* yy //yank-copy line
* dd //delete line
* p //paste-after
* P //paste-before
* u //undo
* . //repeat last command.
* CTRL+v, I, <string>, ESC.	//multi-line editing.


## Auto-completion
* :h ins-completion
* i+<CTRL+X>+<CTRL+I> //all-files-complete
* i+<CTRL+X>+<CTRL+K> //dictionary-complete
	* :set dictionary+=/home/dictionary.txt

## Sequence
Increment sequence: CTRL+v, select sequence range (hjkl), g, CTRL+A.
Decrement sequence: CTRL+v, select sequence range (hjkl), g, CTRL+X.

## Abbreviations
:ab			//list all abbreviations.
:ab abc A B C		//set abbreviation.
:unab abc		//unset abbreviation.

## Marks
:ma A-Z					set mark from A to Z. (multi-files)
'A-Z					go to mark A to Z. (multi-files)

## Macros
q<a-z>					start recording macro to register <a-z>
q						exit recording of macro.
<n>@<a-z>				execute macro <a-z> <n> number of times.



