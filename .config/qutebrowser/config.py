## Super Lean Qutebrowser config.py
config.load_autoconfig(False)
config.set("colors.webpage.darkmode.enabled", True)
c.colors.webpage.bg = '#121419'
c.url.start_pages=('/home/bledley/startpage/index.html')
config.bind(',v', 'hint links spawn mpv {hint-url}')
config.bind(',id', 'hint images download')
config.bind(',iv', 'hint images spawn feh {hint-url}')
config.bind(',b', 'hint links spawn firefox {hint-url}')
config.bind('xb', 'config-cycle statusbar.show always never')
config.bind('xt', 'config-cycle tabs.show always never')
config.bind('xx', 'config-cycle statusbar.show always never;; config-cycle tabs.show always never')
config.bind(',b', 'hint links spawn firefox {hint-url}')
c.colors.tabs.bar.bg = '#262626'
c.colors.tabs.odd.bg = '#262626'
c.colors.tabs.even.bg = '#262626'
c.colors.tabs.selected.odd.bg = '#212121'
c.colors.tabs.selected.even.bg = '#212121'
c.colors.tabs.selected.odd.fg = '#adadad'
c.colors.tabs.selected.even.fg = '#adadad'
c.colors.tabs.odd.fg = '#5e5e5e'
c.colors.tabs.even.fg = '#5e5e5e'
c.colors.hints.bg = '#00A39E'
c.fonts.default_size = '9pt'
c.fonts.completion.entry = '11pt "Terminus"'
c.fonts.debug_console = '9pt "Terminus"'
c.fonts.statusbar = '9pt "Terminus"' 
c.colors.completion.category.bg = '#121419'
c.colors.completion.category.border.bottom = '#191C21'
c.colors.completion.category.border.top = '#191C21'
c.colors.completion.category.fg = '#cccccc'
c.colors.completion.even.bg = '#191C21'
c.colors.completion.fg = ['#BBBBBB', '#ffffff', '#BBBBBB']
c.colors.completion.item.selected.bg = '#009994'
c.colors.completion.item.selected.border.bottom = '#009994'
c.colors.completion.item.selected.border.top = '#009994'
c.colors.completion.item.selected.fg = '#cccccc'
c.colors.completion.item.selected.match.fg = '#ffffff'
c.colors.completion.match.fg = '#ffffff'
c.colors.completion.odd.bg = '#191C21'
c.colors.completion.even.bg = '#191C21'
c.editor.command = ['kitty', '-e', 'nvim', '{file}']
c.tabs.favicons.show = 'never'
c.tabs.title.format = '{current_title}'
c.downloads.location.directory = '/home/bledley/Downloads'
c.url.searchengines = {'DEFAULT': 'https://search.brave.com/search?q={}','dd': 'https://duckduckgo.com/?q={}','aw': 'https://wiki.archlinux.org/?search={}', 'r': 'https://teddit.net/r/{}', 'wik': 'https://wikiless.org/wiki/Main_Page?lang=en/search={}'}
c.aliases = {'w': 'session-save', 'q': 'close', 'qa': 'quit', 'wq': 'quit --save', 'wqa': 'quit --save'}
config.bind('<c>', 'tab-close')
config.bind('<n>', 'tab-next')
config.bind('<p>', 'tab-prev')
config.bind('<r>', 'reload')
config.bind('<t>', 'open -t /home/bledley/startpage/index.html')
config.bind('<1>', 'tab-focus 1')
config.bind('<2>', 'tab-focus 2')
config.bind('<3>', 'tab-focus 3')
config.bind('<4>', 'tab-focus 4')
config.bind('<5>', 'tab-focus 5')
config.bind('<6>', 'tab-focus 6')
c.colors.contextmenu.menu.bg = '#2e3440'
c.colors.contextmenu.menu.fg = '#8a8a8a'
c.colors.contextmenu.selected.bg = '#3e4450'
c.colors.contextmenu.selected.fg = '#D5d5d5'
c.colors.downloads.bar.bg = '#272727'
c.colors.downloads.error.bg = '#b84242'
c.colors.downloads.error.fg = '#b84242'
c.colors.downloads.start.bg = '#6272a4'
c.colors.downloads.stop.bg = '#009994'
c.colors.keyhint.suffix.fg = '#009994'
c.colors.messages.error.bg = '#b84242'
c.colors.prompts.bg = '#272727'
c.colors.prompts.fg = '#7d7d7d'
c.colors.statusbar.caret.bg = '#1e1e1e'
c.colors.statusbar.caret.fg = '#a488ce'
c.colors.statusbar.caret.selection.bg = '#1e1e1e'
c.colors.statusbar.caret.selection.fg = '#7d7d7d'
c.colors.statusbar.command.bg = '#1e1e1e'
c.colors.statusbar.command.fg = '#7d7d7d'
c.colors.statusbar.insert.bg = '#1e1e1e'
c.colors.statusbar.insert.fg = '#00FFF7'
c.colors.statusbar.normal.bg = '#1e1e1e'
c.colors.statusbar.normal.fg = '#7d7d7d'
c.colors.statusbar.private.bg = '#1e1e1e'
c.colors.statusbar.progress.bg = '#7d7d7d'
c.colors.statusbar.url.error.fg = '#fff7Ad'
c.colors.statusbar.url.fg = '#7d7d7d'
c.colors.statusbar.url.hover.fg = '#BBCCDD'
c.colors.statusbar.url.success.http.fg = '#7d7d7d'
c.colors.statusbar.url.success.https.fg = '#7d7d7d'
c.colors.statusbar.url.warn.fg = '#FFF7AD'
c.colors.tabs.indicator.error = '#B84242'
c.colors.tabs.indicator.start = '#009994'
c.colors.tabs.indicator.stop = '#009994'
c.colors.tabs.pinned.even.bg = '#1e1e1e'
c.colors.tabs.pinned.even.fg = '#7d7d7d'
c.colors.tabs.pinned.odd.bg = '#1e1e1e'
c.colors.tabs.pinned.odd.fg = '#7d7d7d'
c.colors.tabs.pinned.selected.even.fg = '#7d7d7d'
c.colors.tabs.pinned.selected.odd.fg = '#7d7d7d'
c.completion.cmd_history_max_items = 5000
c.completion.timestamp_format = '%d-%m-%Y %H:%M'
c.content.blocking.enabled = True
c.content.cookies.accept = 'no-3rdparty'
c.content.geolocation = 'ask'
c.content.media.audio_capture = 'ask'
c.content.media.audio_video_capture = 'ask'
c.content.media.video_capture = 'ask'
c.downloads.position = 'bottom'
c.downloads.remove_finished = 120000
c.fonts.default_family = 'Terminus'
c.fonts.default_size = '8pt'
c.fonts.downloads = 'default_size default_family'
c.fonts.hints = 'bold default_size default_family'
c.fonts.keyhint = 'default_size default_family'
c.fonts.messages.error = 'default_size default_family'
c.fonts.messages.info = 'default_size default_family'
c.fonts.messages.warning = 'default_size default_family'
c.fonts.prompts = 'default_size default_family'
c.fonts.statusbar = 'default_size default_family'
c.fonts.tabs.selected = 'default_size default_family'
c.fonts.tabs.unselected = 'default_size default_family'
c.fonts.web.family.cursive = ''
c.hints.border = '1px solid #009994'
c.hints.leave_on_load = True
c.statusbar.widgets = ['url', 'scroll', 'progress']
c.zoom.levels = ['25%', '33%', '50%', '67%', '75%', '90%', '100%', '110%', '125%', '150%', '175%', '200%', '250%', '300%', '400%', '500%']
config.bind('z', 'zoom-in')
config.bind('x', 'zoom-out')
config.bind('B', 'bookmark-add')
config.bind('d', 'scroll-page 0 0.5')
config.bind('u', 'scroll-page 0 -0.5')
config.bind('gd', 'download')
config.bind('a', 'mode-enter insert')
config.bind('<Ctrl+u>', 'undo')
config.bind(',ap', 'config-cycle content.user_stylesheets ~/.config/qutebrowser/solarized-everything-css/css/apprentice/apprentice-all-sites.css ""')
config.bind(',dr', 'config-cycle content.user_stylesheets ~/.config/qutebrowser/solarized-everything-css/css/darculized/darculized-all-sites.css ""')
config.bind(',gr', 'config-cycle content.user_stylesheets ~/.config/qutebrowser/solarized-everything-css/css/gruvbox/gruvbox-all-sites.css ""')
config.bind(',sd', 'config-cycle content.user_stylesheets ~/.config/qutebrowser/solarized-everything-css/css/solarized-dark/solarized-dark-all-sites.css ""')
config.bind(',sl', 'config-cycle content.user_stylesheets ~/.config/qutebrowser/solarized-everything-css/css/solarized-light/solarized-light-all-sites.css ""')
