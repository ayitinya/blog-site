export interface Blog {
    username: string
    first_name: string
    last_name: string
    id: string
    title: string
    subtitle: string
    body: string
    created_at: string
    author: number

    image?: string
    summary?: string
}

export interface Author {
    id: string
    username: string
    email: string
    first_name: string
    last_name: string
}
