import streamlit as st

# ----------- Setup Page ----------
st.set_page_config(
    page_title="AI Tool Dashboard", 
    layout="wide",
    page_icon="🤖",
    initial_sidebar_state="expanded"
)

# Custom CSS for better styling
st.markdown("""
<style>
    .main-header {
        text-align: center;
        color: #00FFFF;
        font-size: 3rem;
        margin-bottom: 0.5rem;
        text-shadow: 2px 2px 4px rgba(0,255,255,0.3);
    }
    .sub-header {
        text-align: center;
        color: #888888;
        font-size: 1.2rem;
        margin-bottom: 2rem;
    }
    .tool-card {
        padding: 20px;
        margin-bottom: 15px;
        background: linear-gradient(135deg, #1e1e1e 0%, #2d2d2d 100%);
        border-radius: 15px;
        border: 1px solid #333;
        box-shadow: 0 4px 15px rgba(0,255,255,0.1);
        transition: all 0.3s ease;
    }
    .tool-card:hover {
        box-shadow: 0 6px 20px rgba(0,255,255,0.2);
        transform: translateY(-2px);
    }
    .tool-name {
        color: #00FFFF;
        font-size: 1.3rem;
        font-weight: bold;
        margin: 0 0 8px 0;
    }
    .tool-popularity {
        color: #FFD700;
        margin: 5px 0;
        font-size: 0.9rem;
    }
    .tool-link {
        color: #00FFFF;
        text-decoration: none;
        font-weight: 500;
    }
    .tool-link:hover {
        color: #40E0D0;
    }
    .favorite-btn {
        background: linear-gradient(45deg, #FF6B6B, #FF8E8E);
        border: none;
        border-radius: 20px;
        color: white;
        padding: 5px 15px;
        margin-top: 10px;
        cursor: pointer;
        transition: all 0.3s ease;
    }
    .stats-container {
        background: linear-gradient(135deg, #1a1a1a 0%, #2a2a2a 100%);
        padding: 20px;
        border-radius: 15px;
        margin-bottom: 20px;
        border: 1px solid #333;
    }
</style>
""", unsafe_allow_html=True)

# Header
st.markdown('<h1 class="main-header">🤖 AI Tool Recommender Dashboard</h1>', unsafe_allow_html=True)
st.markdown('<p class="sub-header">Discover top AI tools by category. 100+ curated tools!</p>', unsafe_allow_html=True)
st.markdown("---")

# ----------- Initialize Session State ----------
if "favorites" not in st.session_state:
    st.session_state.favorites = []

if "tool_ratings" not in st.session_state:
    # Generate consistent ratings for tools
    st.session_state.tool_ratings = {}

# ----------- Tool Data ----------
ai_tools = {
    "Image": [
        ("Remove.bg", "https://www.remove.bg/", "Remove backgrounds from images instantly"),
        ("DALL·E", "https://openai.com/dall-e", "Generate images from text descriptions"),
        ("Let's Enhance", "https://letsenhance.io/", "AI-powered image upscaling and enhancement"),
        ("RunwayML", "https://runwayml.com/", "Creative AI tools for content creation"),
        ("Clipdrop", "https://clipdrop.co/", "AI-powered visual tools ecosystem"),
        ("DeepArt", "https://deepart.io/", "Transform photos into artworks"),
        ("PhotoRoom", "https://www.photoroom.com/", "Professional product photos in seconds"),
        ("Fotor AI", "https://www.fotor.com/", "AI photo editor and design maker"),
        ("Artbreeder", "https://www.artbreeder.com/", "Collaborative AI art creation"),
        ("Designify", "https://www.designify.com/", "Automatic design generation")
    ],
    
    "Video": [
        ("Pictory", "https://pictory.ai/", "Turn scripts into videos automatically"),
        ("Synthesia", "https://www.synthesia.io/", "AI video generation with avatars"),
        ("Lumen5", "https://www.lumen5.com/", "Transform content into engaging videos"),
        ("Runway", "https://runwayml.com/", "AI-powered video editing suite"),
        ("Descript", "https://www.descript.com/", "Edit videos by editing text"),
        ("Kaiber", "https://www.kaiber.ai/", "AI video generation from text"),
        ("InVideo", "https://invideo.io/", "Create videos with AI assistance"),
        ("Wisecut", "https://www.wisecut.video/", "Automatic video editing"),
        ("Veed.io", "https://www.veed.io/", "Online video editing with AI"),
        ("Animoto", "https://animoto.com/", "Drag-and-drop video maker")
    ],
    
    "Text": [
        ("ChatGPT", "https://chat.openai.com/", "Conversational AI assistant"),
        ("Copy.ai", "https://www.copy.ai/", "AI copywriting assistant"),
        ("Jasper", "https://www.jasper.ai/", "AI content creation platform"),
        ("Writesonic", "https://writesonic.com/", "AI writing and content generation"),
        ("QuillBot", "https://quillbot.com/", "AI paraphrasing and writing tool"),
        ("Sudowrite", "https://www.sudowrite.com/", "AI writing partner for creativity"),
        ("INK Editor", "https://inkforall.com/", "AI content optimization"),
        ("HyperWrite", "https://www.hyperwriteai.com/", "Personal AI writing assistant"),
        ("Rytr", "https://rytr.me/", "AI writing assistant for everyone"),
        ("Scalenut", "https://www.scalenut.com/", "AI-powered SEO and content marketing")
    ],
    
    "Education": [
        ("Khanmigo", "https://www.khanacademy.org/", "AI tutor by Khan Academy"),
        ("Socratic", "https://socratic.org/", "AI-powered homework help"),
        ("Quizgecko", "https://www.quizgecko.com/", "AI quiz and test generator"),
        ("Gradescope AI", "https://gradescope.com/", "AI-assisted grading platform"),
        ("MagicSchool.ai", "https://magicschool.ai/", "AI tools for educators"),
        ("Thinkster Math", "https://hellothinkster.com/", "AI-powered math tutoring"),
        ("Notion AI", "https://www.notion.so/product/ai", "AI writing assistant in Notion"),
        ("Teachology", "https://www.teachology.ai/", "AI lesson planning tool"),
        ("ELI5", "https://eli5.io/", "Explain complex topics simply"),
        ("Mymind", "https://mymind.com/", "AI-powered knowledge management")
    ],
    
    "Marketing": [
        ("AdCreative.ai", "https://www.adcreative.ai/", "AI-generated ad creatives"),
        ("Ocoya", "https://www.ocoya.com/", "AI social media management"),
        ("Postwise", "https://postwise.ai/", "AI Twitter content creation"),
        ("CopyMonkey", "https://copymonkey.ai/", "AI Amazon listing optimization"),
        ("FeedHive", "https://www.feedhive.io/", "AI social media scheduling"),
        ("Surfer SEO", "https://surferseo.com/", "AI-powered SEO optimization"),
        ("MarkCopy", "https://www.markcopy.ai/", "AI marketing copy generation"),
        ("Smartwriter", "https://smartwriter.ai/", "AI cold email personalization"),
        ("Flick", "https://flick.social/", "AI social media assistant"),
        ("Writesonic", "https://writesonic.com/", "AI marketing content creation")
    ],
    
    "Business": [
        ("Tome", "https://tome.app/", "AI-powered storytelling and presentations"),
        ("Beautiful.ai", "https://www.beautiful.ai/", "AI presentation design"),
        ("Decktopus", "https://www.decktopus.com/", "AI presentation creator"),
        ("Durable", "https://durable.co/", "AI website builder for businesses"),
        ("Fireflies", "https://fireflies.ai/", "AI meeting notes and transcription"),
        ("Murf.ai", "https://murf.ai/", "AI voice generator"),
        ("Otter.ai", "https://otter.ai/", "AI meeting transcription"),
        ("Timely", "https://memory.ai/timely", "AI time tracking"),
        ("ClickUp AI", "https://clickup.com/", "AI project management"),
        ("Kuki Chatbot", "https://www.kuki.ai/", "AI chatbot platform")
    ],
    
    "Research": [
        ("Elicit", "https://elicit.org/", "AI research assistant"),
        ("Scite", "https://scite.ai/", "Smart citations and research"),
        ("Consensus", "https://consensus.app/", "AI-powered research engine"),
        ("Semantic Scholar", "https://www.semanticscholar.org/", "AI academic search"),
        ("Research Rabbit", "https://www.researchrabbit.ai/", "AI literature discovery"),
        ("ChatPDF", "https://www.chatpdf.com/", "Chat with PDF documents"),
        ("Scholarcy", "https://www.scholarcy.com/", "AI research summarization"),
        ("ExplainPaper", "https://www.explainpaper.com/", "AI paper explanation"),
        ("Connected Papers", "https://www.connectedpapers.com/", "Visual research exploration"),
        ("Litmaps", "https://www.litmaps.com/", "Literature mapping tool")
    ],
    
    "Chatbots": [
        ("Tidio", "https://www.tidio.com/", "AI customer service chatbot"),
        ("Landbot", "https://landbot.io/", "No-code chatbot builder"),
        ("ChatBot.com", "https://www.chatbot.com/", "AI chatbot platform"),
        ("ManyChat", "https://manychat.com/", "Instagram and Facebook chatbots"),
        ("Drift", "https://www.drift.com/", "Conversational marketing platform"),
        ("Botpress", "https://botpress.com/", "Open-source chatbot platform"),
        ("SnatchBot", "https://www.snatchbot.me/", "Multi-channel chatbot builder"),
        ("MobileMonkey", "https://mobilemonkey.com/", "Facebook Messenger marketing"),
        ("Intercom", "https://www.intercom.com/", "Customer messaging platform"),
        ("Collect.chat", "https://collect.chat/", "Conversational forms and surveys")
    ],
    
    "Design": [
        ("Canva AI", "https://www.canva.com/ai-image-generator/", "AI-powered design platform"),
        ("Looka", "https://looka.com/", "AI logo and brand kit generator"),
        ("Logo AI", "https://www.logoai.com/", "AI logo design tool"),
        ("Designs.ai", "https://designs.ai/", "AI design suite"),
        ("Brandmark", "https://brandmark.io/", "AI logo creation"),
        ("Khroma", "http://khroma.co/", "AI color palette generator"),
        ("Uizard", "https://uizard.io/", "AI UI/UX design tool"),
        ("Visily", "https://www.visily.ai/", "AI wireframe and mockup tool"),
        ("FigJam AI", "https://www.figma.com/figjam/", "AI collaborative whiteboard"),
        ("Cleanup.pictures", "https://cleanup.pictures/", "AI photo cleanup tool")
    ]
}

# Initialize ratings if not exists
for category_tools in ai_tools.values():
    for tool_name, _, _ in category_tools:
        if tool_name not in st.session_state.tool_ratings:
            # Generate consistent ratings based on tool name hash
            import hashlib
            hash_val = int(hashlib.md5(tool_name.encode()).hexdigest(), 16)
            st.session_state.tool_ratings[tool_name] = 3 + (hash_val % 3)  # Rating between 3-5

genres = list(ai_tools.keys())

# ---------- Statistics ----------
total_tools = sum(len(tools) for tools in ai_tools.values())
total_favorites = len(st.session_state.favorites)

col1, col2, col3, col4 = st.columns(4)
with col1:
    st.metric("Total Tools", total_tools, delta=None)
with col2:
    st.metric("Categories", len(genres), delta=None)
with col3:
    st.metric("Your Favorites", total_favorites, delta=None)
with col4:
    avg_rating = sum(st.session_state.tool_ratings.values()) / len(st.session_state.tool_ratings)
    st.metric("Avg Rating", f"{avg_rating:.1f}⭐", delta=None)

st.markdown("---")

# ---------- Sidebar ----------
with st.sidebar:
    st.header("📂 Filter & Options")
    
    # Genre filter
    selected_genre = st.selectbox("Select Category", ["All"] + genres, key="genre_select")
    
    # Search
    search_query = st.text_input("🔍 Search Tools", placeholder="Enter tool name...")
    
    # Sorting options
    sort_option = st.selectbox("Sort by", ["Name (A-Z)", "Name (Z-A)", "Rating (High-Low)", "Rating (Low-High)"])
    
    # Show only favorites
    show_fav = st.checkbox("❤ Show Only Favorites")
    
    # Reset favorites
    if st.button("🔄 Reset All Favorites", type="secondary"):
        st.session_state.favorites = []
        st.rerun()
    
    # Export favorites
    if st.session_state.favorites:
        st.markdown("### 📋 Export Favorites")
        favorites_text = "\n".join([f"• {fav}" for fav in st.session_state.favorites])
        st.text_area("Your Favorites List", favorites_text, height=100)

# ---------- Helper Functions ----------
def get_star_rating(rating):
    return "⭐" * rating + "☆" * (5 - rating)

def toggle_favorite(tool_name):
    if tool_name in st.session_state.favorites:
        st.session_state.favorites.remove(tool_name)
    else:
        st.session_state.favorites.append(tool_name)

def sort_tools(tools, sort_option):
    if sort_option == "Name (A-Z)":
        return sorted(tools, key=lambda x: x[0].lower())
    elif sort_option == "Name (Z-A)":
        return sorted(tools, key=lambda x: x[0].lower(), reverse=True)
    elif sort_option == "Rating (High-Low)":
        return sorted(tools, key=lambda x: st.session_state.tool_ratings.get(x[0], 3), reverse=True)
    elif sort_option == "Rating (Low-High)":
        return sorted(tools, key=lambda x: st.session_state.tool_ratings.get(x[0], 3))
    return tools

def display_tools(tools, category_name="default"):
    if not tools:
        st.info("No tools found matching your criteria.")
        return
    
    # Sort tools
    sorted_tools = sort_tools(tools, sort_option)
    
    # Display in columns
    cols = st.columns(2)
    for i, (name, link, description) in enumerate(sorted_tools):
        rating = st.session_state.tool_ratings.get(name, 3)
        stars = get_star_rating(rating)
        is_favorite = name in st.session_state.favorites
        heart_icon = "❤" if is_favorite else "🤍"
        
        with cols[i % 2]:
            # Create tool card
            st.markdown(f"""
            <div class="tool-card">
                <div class="tool-name">{name} {heart_icon}</div>
                <div class="tool-popularity">{stars} ({rating}/5)</div>
                <p style="color: #CCCCCC; margin: 8px 0; font-size: 0.9rem;">{description}</p>
                <a href="{link}" target="_blank" class="tool-link">🔗 Visit Tool</a>
            </div>
            """, unsafe_allow_html=True)
            
            # Favorite button
            button_key = f"{category_name}{name.replace('.', '').replace('·', '').replace(' ', '')}_{i}"
            if st.button(f"{heart_icon} {'Remove from' if is_favorite else 'Add to'} Favorites", 
                        key=button_key, 
                        type="secondary" if not is_favorite else "primary"):
                toggle_favorite(name)
                st.rerun()

# ---------- Main Content Logic ----------
def get_filtered_tools():
    all_tools = []
    
    if selected_genre == "All":
        for category, tools in ai_tools.items():
            all_tools.extend(tools)
    else:
        all_tools = ai_tools[selected_genre]
    
    # Apply search filter
    if search_query:
        all_tools = [tool for tool in all_tools if search_query.lower() in tool[0].lower()]
    
    # Apply favorites filter
    if show_fav:
        all_tools = [tool for tool in all_tools if tool[0] in st.session_state.favorites]
    
    return all_tools

# Display tools
filtered_tools = get_filtered_tools()

if search_query:
    st.subheader(f"🔍 Search Results for: *{search_query}*")
    if filtered_tools:
        st.write(f"Found {len(filtered_tools)} tool(s)")
    display_tools(filtered_tools, "search")
elif show_fav:
    st.subheader("❤ Your Favorite Tools")
    if filtered_tools:
        st.write(f"You have {len(filtered_tools)} favorite tool(s)")
    else:
        st.info("No favorite tools yet. Start exploring and add some tools to your favorites!")
    display_tools(filtered_tools, "favorites")
elif selected_genre == "All":
    st.subheader("🌟 All AI Tools")
    st.write(f"Showing {len(filtered_tools)} tools across all categories")
    display_tools(filtered_tools, "all")
else:
    st.subheader(f"🔹 {selected_genre} Tools")
    st.write(f"Showing {len(filtered_tools)} tools in {selected_genre} category")
    display_tools(filtered_tools, selected_genre)

# ---------- Footer ----------
st.markdown("---")
st.markdown("""
<div style='text-align: center; color: #666; padding: 20px;'>
    <p>🤖 AI Tool Recommender Dashboard | Built with Streamlit</p>
    <p>Discover, explore, and organize your favorite AI tools!</p>
</div>
""", unsafe_allow_html=True)
