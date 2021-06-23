# shellcheck disable=SC2005
if [ "$1" == "update" ]; then
echo "$(git pull origin master)"
elif [ "$1" == "push" ]; then
  echo "$(git add .)"
  echo "$(git commit -m "script: push by remote server")"
  echo "$(git push -u origin master)"
else
  echo "$1 not available"
fi
