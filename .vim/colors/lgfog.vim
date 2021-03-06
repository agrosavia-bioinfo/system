" Vim color file
" vim: tw=0 ts=4 sw=4
" Maintainer:	Thomas R. Kimpton <tomk@emcity.net>
" Last Change:	2001 Nov 8
" This color scheme is meant for the person that spends hours
" and hours and hours and... in vim and wants some contrast to
" help pick things out in the files they edit, but doesn't want
" **C**O**N**T**R**A**S**T**!

set background=light

hi clear

if exists("syntax_on")
  syntax reset
endif

let colors_name = "lgfog"

hi Normal		ctermfg=Black
hi Normal		gui=bold			guifg=Black			guibg=LightGray

hi NonText		term=bold
hi NonText		ctermfg=LightBlue
hi NonText		gui=bold			guifg=LightBlue			guibg=grey80
" \section \sub...
hi preproc		ctermfg=DarkGray 
" \label, \ref, \url
hi Statement	ctermfg=DarkGray
" inside \section{XXX}
hi Title		cterm=underline ctermfg=DarkBlue ctermbg=Yellow
hi Title		gui=bold			guifg=Blue			guibg=LightSteelBlue
" inside of label|ref|url...
hi Special 		cterm=bold		ctermfg=DarkMagenta	

" Folded text
hi Folded		ctermbg=Gray	ctermfg=LightBlue
" Spelling
hi SpellBad     guibg=Red   guifg=Black



hi Comment		ctermfg=LightBlue
"hi Comment		ctermfg=LightGrey	ctermbg=White
" 444499 = darkish blue grey
hi Comment		guifg=#444499

hi Constant		term=underline
hi Constant		ctermfg=Magenta
hi Constant		guifg=#7070a0

hi identifier	ctermfg=DarkGreen
hi identifier	guifg=DarkGreen

hi type			ctermfg=DarkBlue
hi type			guifg=DarkBlue

hi label		ctermfg=yellow
hi label		guifg=#c06000

hi operator		ctermfg=darkYellow
hi operator		guifg=DarkGreen		gui=bold

hi StorageClass	ctermfg=DarkBlue			ctermbg=White
hi StorageClass	guifg=#a02060			gui=bold

hi Number		ctermfg=Blue		ctermbg=White
hi Number		guifg=Blue

hi Cursor		ctermbg=DarkMagenta
hi Cursor		guibg=#880088		guifg=LightGrey

hi lCursor		guibg=Cyan			guifg=Black

hi ErrorMsg		term=standout
hi ErrorMsg		ctermbg=DarkBlue		ctermfg=White
hi ErrorMsg		guibg=DarkBlue		guifg=White

hi DiffText		term=reverse
hi DiffText		cterm=bold			ctermbg=DarkBlue
hi DiffText		gui=bold			guibg=DarkBlue

hi Directory	term=bold
hi Directory	ctermfg=LightBlue
hi Directory	guifg=Blue gui=underline

hi LineNr		term=underline
hi LineNr		ctermfg=Yellow
hi LineNr		guifg=#ccaa22

hi MoreMsg		term=bold
hi MoreMsg		ctermfg=LightGreen
hi MoreMsg		gui=bold			guifg=SeaGreen

hi Question		term=standout
hi Question		ctermfg=LightGreen
hi Question		gui=bold			guifg=DarkGreen

hi Search		term=reverse
hi Search		ctermbg=DarkYellow	ctermfg=Black
hi Search		guibg=#887722		guifg=Black

hi SpecialKey	term=bold
hi SpecialKey	ctermfg=LightBlue
hi SpecialKey	guifg=Blue

hi SpecialChar	ctermfg=DarkGrey	ctermbg=White
hi SpecialChar	guifg=DarkGrey		gui=bold

hi WarningMsg	term=standout
hi WarningMsg	ctermfg=LightBlue
hi WarningMsg	guifg=DarkBlue		guibg=#9999cc

hi WildMenu		term=standout
hi WildMenu		ctermbg=Yellow		ctermfg=Black
hi WildMenu		guibg=Yellow		guifg=Black gui=underline

hi FoldColumn	term=standout
hi FoldColumn	ctermbg=LightGrey	ctermfg=DarkBlue
hi FoldColumn	guibg=Grey			guifg=DarkBlue

hi DiffAdd		term=bold
hi DiffAdd		ctermbg=DarkBlue
hi DiffAdd		guibg=DarkBlue

hi DiffChange	term=bold
hi DiffChange	ctermbg=DarkMagenta
hi DiffChange	guibg=DarkMagenta

hi DiffDelete	term=bold
hi DiffDelete	ctermfg=Blue		ctermbg=DarkCyan
hi DiffDelete	gui=bold			guifg=Blue			guibg=DarkCyan

hi Ignore		ctermfg=LightGrey
hi Ignore		guifg=grey90

hi IncSearch	term=reverse
hi IncSearch	cterm=reverse
hi IncSearch	gui=reverse

hi ModeMsg		term=bold
hi ModeMsg		cterm=bold
hi ModeMsg		gui=bold

hi StatusLine	term=reverse,bold
hi StatusLine	cterm=reverse,bold
hi StatusLine	gui=reverse,bold

hi StatusLineNC	term=reverse
hi StatusLineNC	cterm=reverse
hi StatusLineNC	gui=reverse

hi VertSplit	term=reverse
hi VertSplit	cterm=reverse
hi VertSplit	gui=reverse

hi Visual		term=reverse
hi Visual		cterm=reverse
hi Visual		gui=reverse			guifg=DarkGrey		guibg=fg

hi VisualNOS	term=underline,bold
hi VisualNOS	cterm=underline,bold
hi VisualNOS	gui=underline,bold

hi Todo			gui=reverse

" vim: sw=2
