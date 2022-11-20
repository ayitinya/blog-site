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

    image: string
    summary: string

    tags: Tag[]

}

export interface Author {
    id: string
    username: string
    email: string
    first_name: string
    last_name: string
    image: string
    bio: string
    social_links: SocialLink[]
}

export interface SocialLink {
    name: string
    url: string
}

export interface Tag {
    id: string
    name: string
}
