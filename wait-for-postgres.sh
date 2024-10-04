#!/bin/sh

set -e

host="$1"
port="$2"
shift 2

until pg_isready -h "$host" -p "$port"; do
  echo "Postgres is unavailable - sleeping"
  sleep 1
done

echo "Postgres is up - executing command"
exec "$@"
