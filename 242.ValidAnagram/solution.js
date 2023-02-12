/**
 * @param {string} s
 * @param {string} t
 * @return {boolean}
 */

function isAnagram(s, t) {
  if (s.length !== t.length) return false;

  const count = {};

  for (let i = 0; i < s.length; i++) {
    if (!count[s[i]]) count[s[i]] = 0;
    if (!count[t[i]]) count[t[i]] = 0;
    count[s[i]]++;
    count[t[i]]--;
  }
  for (let c in count) {
    if (count[c] !== 0) return false;
  }
  return true;
}
