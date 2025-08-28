function neutralise(s1, s2) {
//    const arr1 = s1.split('');
//     const arr2 = s2.split('');
//     let res = '';
//     for (let i = 0; i < arr1.length; i++) {
//         const charOfArr1 = arr1[i];
//         const charOfArr2 = arr2[i];
//             if (charOfArr1 !== charOfArr2) {
//                 res += '0';
//             } else {
//                 res += charOfArr1;
//         }
//     }
//     return res;
  return s1.split('').map((char, i)=> char === s2[i] ? char : '0').join('')
}