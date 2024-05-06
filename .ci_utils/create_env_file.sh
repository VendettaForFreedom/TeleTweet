if [ -e env/teletweet.env ]; then
    rm env/teletweet.env
fi
touch env/teletweet.env
echo TOKEN=\"${TOKEN}\" > env/teletweet.env
echo CONSUMER_KEY=\"${CONSUMER_KEY}\" >> env/teletweet.env
echo CONSUMER_SECRET=\"${CONSUMER_SECRET}\" >> env/teletweet.env
echo APP_ID=\"${APP_ID}\" >> env/teletweet.env
echo APP_HASH=\"${APP_HASH}\" >> env/teletweet.env
echo ACCESS_KEY=\"${ACCESS_KEY}\" >> env/teletweet.env
echo ACCESS_SECRET=\"${ACCESS_SECRET}\" >> env/teletweet.env
echo CONFIG_CHANNEL_ID=\"${CONFIG_CHANNEL_ID}\" >> env/teletweet.env
echo CHANNEL_ID=\"${CHANNEL_ID}\" >> env/teletweet.env
echo SOURCE_CHANNEL_ID=\"${SOURCE_CHANNEL_ID}\" >> env/teletweet.env
echo GROUP_ID=\"${GROUP_ID}\" >> env/teletweet.env
echo ALLOW_USER=\"${ALLOW_USER}\" >> env/teletweet.env

