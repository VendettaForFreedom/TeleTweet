#!/bin/bash

# Define the image name
IMAGE_NAME=$1

# List all tags for the image
TAGS=$(docker images --format "{{.Repository}}:{{.Tag}}" | grep "^${IMAGE_NAME}:")


echo tags: $TAGS

# Extract the latest tag
LATEST_TAG=$(echo "$TAGS" | head -n 1)
echo latest_tag: $LATEST_TAG

# Number of tags to keep (including the latest one)
KEEP=1
# # Extract tags to be deleted
TAGS_TO_DELETE=$(echo "$TAGS" | tail -n +$(($KEEP + 1)))

echo tags_to_delete: $TAGS_TO_DELETE
for tag in $TAGS_TO_DELETE; do
    echo "Removing image: $tag"
    docker rmi "$tag"
done
