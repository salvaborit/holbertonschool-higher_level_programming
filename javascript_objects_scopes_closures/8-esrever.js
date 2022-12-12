#!/usr/bin/node

exports.esrever = function (list) {
  let start = 0;
  let end = list.length - 1;
  const arr = [...list];

  for (; start < list.length; start++) {
    arr[start] = list[end];
    end--;
  }

  return arr;
};
