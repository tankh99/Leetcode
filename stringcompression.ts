function compress(chars: string[]): number {
    let s = "";
    let count = 0;
    for (let i = 0; i < chars.length - 1; i++) {
        if (chars[i] === chars[i + 1]) {
            count++;
        } else {
            s += chars[i]
            if (count > 1) {
                s += count;
            }
            count = 0;
        }
    }
    console.log(s)
    return s.length;
};


compress(["a","b", "b"])