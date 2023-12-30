const fs             = require('fs');
const { mdToPdf }    = require('md-to-pdf')

const makePDF = async (markdown, invoice) => {
    let mdFile = `/app/static/user_files/markdown/${invoice}.md`;
    let pdfFile = `/app/static/user_files/pdf/${invoice}.pdf`;

    fs.writeFileSync(mdFile, markdown);

    return new Promise(async (resolve, reject) => {
        try {
            await mdToPdf(
                { content: markdown },
                {
                    dest: pdfFile,
                    stylesheet: '/app/static/css/invoiceStyles.css',
                    launch_options: { args: ['--no-sandbox', '--js-flags=--noexpose_wasm,--jitless'] }
                }
            );
            resolve();
        } catch (e) {
            reject(e);
        }
    });
}

module.exports = {
    makePDF
};