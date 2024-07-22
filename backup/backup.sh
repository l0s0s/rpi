#!/bin/bash

SOURCE_DIR="/home/pi"

DEST_DIR="/mnt/backup"

BACKUP_FILE="$DEST_DIR/backup_$(date +%Y%m%d_%H%M%S).tar.gz"

tar -czvf $BACKUP_FILE $SOURCE_DIR

find $DEST_DIR -name "*.tar.gz" -type f -mtime +7 -exec rm -f {} \;

echo "Резервное копирование завершено: $BACKUP_FILE"
