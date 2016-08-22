# vim-radio
Listen to internet radio in neovim

### What is this
With this plugin you are able to listen to radio-streams inside your favorite text editor.
It currently only works on OSX and Neovim, but as soon as i learn vimscript i will rework it (eventually).

### Installation
You need to have VLC and Neovim installed.
copy vim-radio.py into ~/.config/nvim/autoload/vim-radio/ and edit the streamlist to contain your favorite streams 
in the form of ["http://www.blabla.m3u", "http://somethingelse.m3u", "http://iTriedOnlyM3U.m3u].

To be able to listen to the music in background we need the async jobs from neovim, and for convenience you can 
add the following to your nvim dotfiles.  
```vim
nmap <leader>r :let job1 = jobstart(['bash','-c','python3 ~/.config/nvim/autoload/vim-radio/Plugin.py 0'])
nmap <leader>s :call jobstop(job1)<CR>
```
When you press <leader>r you can either listen to the first stream provided, by pressing <CR> or changing the '0' to any
index of your stream.
With <leader>s you can stop playing the radio.

Feel free to tell me how to make better code, i have literally no experience in writing vim Plugins
