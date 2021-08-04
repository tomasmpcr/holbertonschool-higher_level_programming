#!/usr/bin/node

exports.nbOccurences = function (list, searchElement) {
  let contador = 0;
  for (let i = 0; i <= list.length; i++) {
    if (list[i] === searchElement) {
      contador++;
    }
  }
  return (contador);
};
