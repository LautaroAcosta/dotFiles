-- This file can be loaded by calling `lua require('plugins')` from your init.vim

-- Only required if you have packer configured as `opt`
vim.cmd [[packadd packer.nvim]]

return require('packer').startup(function()
    -- Package Manager
    use 'wbthomason/packer.nvim'
    
    -- Plugin para Latex
    use 'lervag/vimtex'
    
    -- Tema de color
    use 'sainnhe/gruvbox-material'
    
    -- Plugin para configurar la apariencia del editor
    use {
        "windwp/nvim-autopairs",
    config = function() require("nvim-autopairs").setup {} end
    }
    use 'tpope/vim-commentary'
    use "lukas-reineke/indent-blankline.nvim"
    -- use 'vim-airline/vim-airline'
    -- use 'vim-airline/vim-airline-themes'
    use {
    'nvim-lualine/lualine.nvim',
     requires = { 'kyazdani42/nvim-web-devicons', opt = true }
    }
    use 'ryanoasis/vim-devicons'
    use 'p00f/nvim-ts-rainbow'
    use 'nvim-tree/nvim-web-devicons'
    use 'ap/vim-css-color'
    -- NERDTree  
    use 'scrooloose/nerdtree'

    use 'tiagofumo/vim-nerdtree-syntax-highlight'
        
    -- TreeSitter
    use {'nvim-treesitter/nvim-treesitter', run = ":TSUpdate",}

    -- Configuración para los servidores de lenguaje
    use 'neovim/nvim-lspconfig'
    use 'williamboman/nvim-lsp-installer'
    use 'hrsh7th/cmp-nvim-lsp'
    use 'hrsh7th/cmp-buffer'
    use 'hrsh7th/cmp-path'
    use 'hrsh7th/cmp-cmdline'
    use 'hrsh7th/nvim-cmp'
    use 'saadparwaiz1/cmp_luasnip' -- Snippets source for nvim-cmp
    use 'L3MON4D3/LuaSnip' -- Snippets plugin
    
    -- Telescope, File Finder
    use {
        'nvim-telescope/telescope.nvim', tag = '0.1.0',
      requires = { {'nvim-lua/plenary.nvim'} }
    }
        use 'nvim-telescope/telescope-file-browser.nvim'

    -- ToggleTerm, Terminal adentro de nvim
    -- use "akinsho/toggleterm.nvim"

    -- Startup Info
    use 'dstein64/vim-startuptime'

    --VimWiki
    use 'vimwiki/vimwiki'

    --QuickSearch
    use 'justinmk/vim-sneak'
    
    -- Autosave
    use({
	"Pocco81/auto-save.nvim",
	config = function()
		 require("auto-save").setup {
			-- your config goes here
			-- or just leave it empty :)
	     }
	end,
})
end)

