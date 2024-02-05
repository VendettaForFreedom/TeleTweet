if [ -e env/teletweet.env ]; then
    rm env/teletweet.env
fi
echo TOKEN=${{ secrets.TOKEN}} >> env/teletweet.env
echo CONSUMER_KEY=${{ secrets.CONSUMER_KEY}} >> env/teletweet.env
echo CONSUMER_SECRET=${{ secrets.CONSUMER_SECRET}} >> env/teletweet.env
echo #CALLBACK_URL=  >> env/teletweet.env
echo APP_ID=${{ secrets.APP_ID}} >> env/teletweet.env
echo APP_HASH=${{ secrets.APP_HASH}} >> env/teletweet.env
echo ACCESS_KEY=${{ secrets.ACCESS_KEY}} >> env/teletweet.env
echo ACCESS_SECRET=${{ secrets.ACCESS_SECRET}} >> env/teletweet.env
echo CONFIG_CHANNEL_ID=${{ secrets.CONFIG_CHANNEL_ID}} >> env/teletweet.env
echo CHANNEL_ID=${{ secrets.CHANNEL_ID}} >> env/teletweet.env
echo ALLOW_USER=${{ secrets.ALLOW_USER}} >> env/teletweet.env

