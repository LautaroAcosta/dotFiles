require("mason").setup()
require("mason-lspconfig").setup({
    ensure_installed = {"sumneko_lua", "clangd", "jedi_language_server", "rust_analyzer", "texlab", "gopls", "tsserver","cssls","html"}
})

local capabilities = require('cmp_nvim_lsp').default_capabilities()

require('lspconfig')['jedi_language_server'].setup {
    capabilities = capabilities
  }

  require('lspconfig')['clangd'].setup {
    capabilities = capabilities
  }

   require('lspconfig')['rust_analyzer'].setup {
    capabilities = capabilities
  }

   require('lspconfig')['texlab'].setup {
    capabilities = capabilities
  }


   require('lspconfig')['gopls'].setup {
    capabilities = capabilities
  }

  require('lspconfig')['sumneko_lua'].setup{
      capabilities = capabilities
  }

 require('lspconfig')['tsserver'].setup {
    capabilities = capabilities
  }
  
 require('lspconfig')['cssls'].setup {
    capabilities = capabilities
  }

 require('lspconfig')['html'].setup {
    capabilities = capabilities
  }





