-- This file can be loaded by calling `lua require('plugins')` from your init.vim

-- Only required if you have packer configured as `opt`
vim.cmd [[packadd packer.nvim]]

return require('packer').startup(function()
  -- Packer can manage itself
  use 'wbthomason/packer.nvim'
  use 'lervag/vimtex'
  use 'sainnhe/gruvbox-material'
  use {
	"windwp/nvim-autopairs",
    config = function() require("nvim-autopairs").setup {} end
    }
  use 'tpope/vim-commentary'
  use "lukas-reineke/indent-blankline.nvim"
  use 'vim-airline/vim-airline'
  use 'vim-airline/vim-airline-themes'
  use 'ryanoasis/vim-devicons'
  use 'tiagofumo/vim-nerdtree-syntax-highlight'
  use 'scrooloose/nerdtree'
  use {'nvim-treesitter/nvim-treesitter', run = ":TSUpdate",}
  use 'p00f/nvim-ts-rainbow'

  -- use 'ms-jpq/coq_nvim'
  -- use 'ms-jpq/coq.artifacts'
  use 'neovim/nvim-lspconfig'
  use 'williamboman/nvim-lsp-installer'
  
  use 'hrsh7th/cmp-nvim-lsp'
  use 'hrsh7th/cmp-buffer'
  use 'hrsh7th/cmp-path'
  use 'hrsh7th/cmp-cmdline'
  use 'hrsh7th/nvim-cmp'
  use 'saadparwaiz1/cmp_luasnip' -- Snippets source for nvim-cmp
  use 'L3MON4D3/LuaSnip' -- Snippets plugin
  -- use 'mhinz/vim-startify'
  use 'nvim-tree/nvim-web-devicons'
  use {
  'nvim-telescope/telescope.nvim', tag = '0.1.0',
-- or                            , branch = '0.1.x',
      requires = { {'nvim-lua/plenary.nvim'} }
}

    local builtin = require('telescope.builtin')
vim.keymap.set('n', '<leader>ff', builtin.find_files, {})
vim.keymap.set('n', '<leader>fg', builtin.live_grep, {})
vim.keymap.set('n', '<leader>fb', builtin.buffers, {})
vim.keymap.set('n', '<leader>fh', builtin.help_tags, {})

  use 'ap/vim-css-color'


  -- use 'junegunn/goyo.vim'
  -- use 'junegunn/limelight.vim'

 use 'nvim-telescope/telescope-media-files.nvim'


end)

