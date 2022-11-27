vim.g.mapleader= " "
vim.opt.guicursor = ""
vim.cmd [[set mouse=a]]
vim.opt.nu = true
vim.opt.relativenumber = true

vim.opt.tabstop = 4
vim.opt.softtabstop = 4
vim.opt.shiftwidth = 4
vim.opt.expandtab = true
vim.opt.hlsearch = false
vim.opt.incsearch = true

vim.opt.smartindent = true
vim.opt.scrolloff = 8
vim.opt.showcmd = true

vim.opt.spellsuggest = best , 5
vim.opt.wrap = false

vim.opt.list = true
vim.opt.listchars:append "eol:↴"

vim.opt.spell = es

vim.cmd[[
    setlocal spell spelllang=es
    setlocal spell!
 ]]

vim.keymap.set('n', '<leader>s', ':setlocal spell!<CR>')
vim.keymap.set('n','<F2>',':NERDTreeToggle<CR>')
