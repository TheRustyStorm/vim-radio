# vim-radio
Listen to internet radio in vim8/neovim

### What is this
With this plugin you are able to listen to radio-streams inside your favorite text editor on Unix.
### Installation
You need to have VLC and vim8/Neovim installed.

You may install via vim-plug, if you insert the following in your dotfile.
```vim
Plug 'TheSovietStorm/vim-radio'
```
The manual way would be to copy vim-radio.py into ~/.config/nvim/autoload/vim-radio/vim-radio/ 

### Adding Streams
Add your desired Stream to streams.csv in ~/.config/nvim/autoload/vim-radio/vim-radio in the form of:
```csv
"http://www.blabla.m3u"
"http://somethingelse.m3u"
"http://iTriedOnlyM3U.m3u"
```

To be able to listen to the music in background we need the async jobs, and for convenience you can 
add the following to your dotfiles (Edit the path to your Plugins, if they are in other locations).  
### VIM
```vim
nmap <leader>r :let job1 = job_start(['bash','-c','python3 ~/.vim/plugged/vim-radio/vim-radio/vim-radio.py 0'])
nmap <leader>s :call job_stop(job1)<CR>
```
### NEOVIM
```vim
nmap <leader>r :let job1 = jobstart(['bash','-c','python3 ~/.config/nvim/autoload/vim-radio/vim-radio/vim-radio.py 0'])
nmap <leader>s :call jobstop(job1)<CR>
```

When you press <leader>r you can either listen to the first stream provided, by pressing <CR> or changing the '0' to any
index of your stream.
With <leader>s you can stop playing the radio.

Feel free to tell me how to make better code, i have literally no experience in writing vim Plugins
