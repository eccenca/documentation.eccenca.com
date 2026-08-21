#!/bin/bash -x

output_dir_rules=/home/karima/datasets/rules

mkdir -p  ${output_dir_rules}
cd ${output_dir_rules}
git clone --depth 1 https://github.com/Yamato-Security/hayabusa-rules
git clone --depth 1 https://github.com/SigmaHQ/sigma

for file in $(find . -name '*.yml'); do
    [ -f "$file" ] || break
	yq ".rulePath = \"${file}\"" -o=json  $file > ${file}.json
done
