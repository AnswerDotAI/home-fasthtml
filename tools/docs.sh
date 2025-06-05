#!/usr/bin/env bash
set -eux

pushd ../fasthtml
nbdev_docs
popd
cp -r ../fasthtml/_docs/* docs/
tools/sitemap.py
git add -A
git status

