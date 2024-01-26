# sundaymorning
A fediverse bot that posts a single media file as configured and nothing else

## Usage
Run ```login.py```, and give it your bot's account info, so it can generate the token files. Once you've ran that, you can run ```post.py``` each time you want the bot to post, using something like cron.

To change the post's content, simply edit ```config.ini```.

You should enable the ```DryRun``` option if you want to test your configuration. Make sure to disable it to start actually posting!