const lst = [
  {
    a: 'a',
    b: 'b',
    l: [{ c: 'c' }],
  },
];

lst.forEach((item) => {
  delete item.a;
  //   delete item.l[0].c;
});

console.log(lst);

/*
MO
TU
WE
TH

*/
