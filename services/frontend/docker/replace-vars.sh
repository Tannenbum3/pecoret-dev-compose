#!/bin/sh
# @see https://stackoverflow.com/questions/18185305/storing-bash-output-into-a-variable-using-eval
ROOT_DIR=/app/dist
          
# Replace env vars in JavaScript files
echo "Replacing env constants in JS"

keys="VITE_APP_API_URL"

for file in $ROOT_DIR/assets/index*.js* ;
do
  echo "Processing $file ...";
  for key in $keys
  do
    value=$(eval echo \$$key)
    echo "replace $key by $value"
    sed -i 's#'"$key"'#'"$value"'#g' $file
    sleep 10
  done
done

