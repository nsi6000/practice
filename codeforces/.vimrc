
set nocompatible
filetype off

if has('syntax')
  syntax on
endif

set number

abbr psvm public static void main(String[] args){<CR>}<esc>0
abbr sop System.out.println("");<esc>2hi
abbr fori for(int i = 0; i < ; i++){}<esc>i
abbr fore for(char c : s.toCharArray()){}<esc>i
abbr ari int[] a = new int[n];<esc>
abbr ali ArrayList<Integer> al = new ArrayList<>;<esc>
abbr hsi HashSet<Integer> hs = new HashSet<>();<esc>
abbr hmii HashMap<Integer, Integer> hm = new HashMap<>();<esc>

map <F3> <esc>:!time java -Xmx256M main < test<CR>
map <F4> <esc>:!clang-format -i %<CR>
map <F5> <esc>:!javac %<CR>
map <F6> <esc>:!java % < test<CR>
map <F7> <esc>:!java -Xmx256M % < test<CR>
map <F8> <esc>:!java -Xmx256M %<CR>
map <F9> <esc>:!java -Xmx256M % < test <bar> diff -c result -<CR>
map <F10> <esc>:!java %<CR>
