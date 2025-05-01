module.exports = {
    plugins: [
        { name: 'removeDoctype', active: true },
        { name: 'removeXMLProcInst', active: true },
        { name: 'removeComments', active: true },
        { name: 'removeMetadata', active: true },
        { name: 'removeEditorsNSData', active: true },
        { name: 'cleanupAttrs', active: true },
        { name: 'convertColors', params: { currentColor: true } },
        { name: 'removeEmptyAttrs', active: true },
        { name: 'collapseGroups', active: true },
        { name: 'removeUnusedNS', active: true },
        { name: 'removeUselessStrokeAndFill', active: true },
        { name: 'cleanupNumericValues', params: { floatPrecision: 2 } }
    ]
};
