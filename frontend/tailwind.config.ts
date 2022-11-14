import type { Config } from 'tailwindcss'


export default <Partial<Config>>{
    plugins: [
        require('@tailwindcss/line-clamp'),
        require('@tailwindcss/typography'),
        require('@tailwindcss/forms'),
    ]
}