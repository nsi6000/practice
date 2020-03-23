# Vim
<https://vimawesome.com/>
<https://vim.fandom.com/>

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
* :!<command> //execute-shell-command

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

## Auto-completion
* :h ins-completion
* i+<CTRL+X>+<CTRL+I> //all-files-complete
* i+<CTRL+X>+<CTRL+K> //dictionary-complete
	* :set dictionary+=/home/dictionary.txt


