# Vim
## Websites
* <https://vimawesome.com/>
* <https://vim.fandom.com/>
* <https://github.com/mhinz/vim-galore>

* vim file1 +line_number		open file at specified line number.
* vim -o file1 file2		vertical window.
* vim -O file1 file2		horizontal window.
	* C-w-w			change window.
* CTRL+w hjkl			switch window.


## Commands
* :help <command> :q //help
* :read !ls *pdf //input list of PDF files
* :r !ls //short-version of :read
* :sort //sort the whole file
* :sort u //sort and remove duplicates for the whole file
* :sort n //numerci sort
* :1,5 sort //sort from line 1 to 5
* :color-scheme industry //change color scheme to Industry theme
* "*yy //copy to primary
* "*p //paster from primary
* "+yy //copy to clipboard
* "+p //paster from clipboard
* :wq //write-quit
* :x //idem
* :q! //discard-quit
* :w //write-save
* :xa //write-quit all files
* :qa! //discard-quit all files
* :e <file> #edit file
* :sp //split
* :vs //vertical-split
* CTRL + ww #switch panes
* ctrl + w + hjkl #switch panes
* :set number //activate-line-numbering
* :set cursorline //activate-cursor-line
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
* :r <file>		//read file.
* :his			//history of commands.
* :h <string>		//show help of <string>.
* :!indent % + (L)oad.	//execute indent on current file.
* :make %<		//execute make.

Number|   Operator   |Motion
0-999 |iao xcrd yp u.|0$bw hjkl

* i //insert-mode
* a //append-cursor
* A //append-EOL
* o //newline-after
* O //newline-before

* x //delete character
* cw //change word
* 5cw //change 5 words
* c$ //change until EOL
* 5c$ //change 5 lines until EOL
* r //replace one character
* R //replace multiple characters
* d //delete character
* dw //delete word
* d5w //delete 5 words
* d$ //delete until EOL
* d0 //delete until BOL
* dgg //delete until EOF
* dG //delete until BOF

* 0 //move-BOL
* $ //move-EOL
* b //move-previous-word
* w //move-next-word
* gg //move-BOF
* GG //move-EOF
* 42gg //move-to-line-number
* 5w //move 5 words
* 5j //move down 5 lines

* v //visual-mode
* yy //yank-copy line
* 5yy //yank-copy 5 lines
* dd //delete line
* 5dd //delete 5 lines
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
* Increment sequence: CTRL+v, select sequence range (hjkl), g, CTRL+A.
* Decrement sequence: CTRL+v, select sequence range (hjkl), g, CTRL+X.

## Abbreviations
* :ab			//list all abbreviations.
* :ab abc A B C		//set abbreviation.
* :unab abc		//unset abbreviation.

## Marks
* :ma A-Z					set mark from A to Z. (multi-files)
* 'A-Z					go to mark A to Z. (multi-files)

## Macros
* q<a-z>					start recording macro to register <a-z>
* q						exit recording of macro.
* <n>@<a-z>				execute macro <a-z> <n> number of times.

## Set spelling language
* " spelling
* set spellfile =~/.vim/spell/en.utf-8.add,~/.vim/spell/de.utf-8.add
* set spelllanf =en,de


## comment lines for python
```
ctrl+v
selected lines
shift + I
# + space
esc
```

## todo
```
ctrl + v
select items
shift + X
.
```

## indent lines with tabs
```
shift + v
select lines
shift + >>
.....
```

## todo
```
CTRL + Z
jobs
fg %2
```


