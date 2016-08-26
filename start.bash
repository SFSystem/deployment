#/bin/bash

echo "Starting project"
MAIN_DIR=`pwd`

if [ -d ${MAIN_DIR}/../sfsystem ]
then
    mkdir -p ${MAIN_DIR}/static
    mkdir -p ${MAIN_DIR}/media
    mkdir -p ${MAIN_DIR}/media/avatars
    mkdir -p ${MAIN_DIR}/media/mailmessages
    mkdir -p ${MAIN_DIR}/media/manufacturer_logo
    mkdir -p ${MAIN_DIR}/media/partner_card_logo
    mkdir -p ${MAIN_DIR}/media/shop_logo
    mkdir -p ${MAIN_DIR}/media/shop_product

    mkdir -p ${MAIN_DIR}/../sfsystem/apps
    touch ${MAIN_DIR}/../sfsystem/apps/__init__.py

    mkdir -p ${MAIN_DIR}/../templates

    echo "Finished project"
else
    echo "SFSystem library not found."
fi