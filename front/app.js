const { createApp } = Vue;

createApp({
    data() {
        return {
            products: [],
            newProduct: { name: '', price: '' },
            stats: {
                highest: {},
                lowest: {},
                average: 0
            },
            aboveAverage: [],
            belowAverage: []
        }
    },
    mounted() {
        this.loadData();
    },
    methods: {
        async loadData() {
            try {
                const responses = await Promise.all([
                    axios.get('/products'),
                    axios.get('/products/highest'),
                    axios.get('/products/lowest'),
                    axios.get('/products/average'),
                    axios.get('/products/above-average'),
                    axios.get('/products/below-average')
                ]);

                this.products = responses[0].data;
                this.stats.highest = responses[1].data;
                this.stats.lowest = responses[2].data;
                this.stats.average = responses[3].data.average?.toFixed(2) || 0;
                this.aboveAverage = responses[4].data;
                this.belowAverage = responses[5].data;
            } catch (error) {
                console.error('Error loading data:', error);
            }
        },

        async addProduct() {
            if (!this.newProduct.name || !this.newProduct.price) return;

            try {
                await axios.post('/products', null, {
                    params: {
                        name: this.newProduct.name,
                        price: parseFloat(this.newProduct.price)
                    }
                });

                this.newProduct = { name: '', price: '' };
                await this.loadData();
            } catch (error) {
                alert('Error adding product');
            }
        },

        async deleteProduct(id) {
            if (confirm('Delete this product?')) {
                try {
                    await axios.delete(`/products/${id}`);
                    await this.loadData();
                } catch (error) {
                    alert('Error deleting product');
                }
            }
        }
    }
}).mount('#app');